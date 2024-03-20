#!/usr/bin/env python
from flask import Flask, request, jsonify
from waitress import serve
import os
import json
import pickle

import handler

app = Flask(__name__)


class Event:
    def __init__(self):
        self.body = request.get_data()
        self.headers = request.headers
        self.method = request.method
        self.query = request.args
        self.path = request.path

    def to_dict(self):
        body_dict = json.loads(self.body.decode("utf-8")) if self.body else {}

        return {
            "body": body_dict,
            "headers": dict(self.headers),
            "method": self.method,
            "query": dict(self.query),
            "path": self.path,
        }


class Context:
    def __init__(self):
        self.hostname = os.getenv("HOSTNAME", "localhost")


def format_status_code(resp):
    if "statusCode" in resp:
        return resp["statusCode"]

    return 200


def format_body(resp):
    return pickle.loads(resp.get("body", None))


def format_headers(resp):
    headers = [("Contenty-Type", "text/plain")]

    if "headers" not in resp:
        return headers
    elif type(resp["headers"]) == dict:
        for key in resp["headers"].keys():
            header_tuple = (key, resp["headers"][key])
            headers.append(header_tuple)
        return headers

    return headers


def format_response(resp):
    if resp == None:
        return ("", 200)

    statusCode = format_status_code(resp)
    body = format_body(resp)
    headers = format_headers(resp)

    return (body, statusCode, headers)


@app.route(
    "/", defaults={"path": ""}, methods=["GET", "PUT", "POST", "PATCH", "DELETE"]
)
@app.route("/<path:path>", methods=["GET", "PUT", "POST", "PATCH", "DELETE"])
def call_handler(path):
    event = Event()
    context = Context()
    response_data = handler.handle(event.to_dict(), context)

    resp = format_response(response_data)
    return resp


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)

### **Using Custom Templates with OpenFaaS**

#### 1. **Download Custom Templates:**

- Execute the following command to download available templates:
  ```bash
  faas-cli template pull https://github.com/singnet/das-openfaas-templates.git
  ```

#### 2. **Available Templates:**

- Our repository offers various templates to cater to different needs. Below are some of the available templates:

##### a. **Python 3 Template:**

      - Developed to reuse functions across different serverless services. Maintains the structure outside the `function` folder to facilitate the import of files with relative paths.

#### 3. **Developing Functions:**

- Create new functions in the appropriate directory and choose the template that suits your needs.

This documentation provides information about the available templates and guides users in developing functions with the chosen template.

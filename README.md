## Create Azure Functions App
1. Go to [Azure Portal](https://portal.azure.com/#create/Microsoft.FunctionApp)
2. Select **Consumption**
3. Enter your Subscription, Resource Group. Create a new one if you don’t have any.

**Configuration:**
- **Function App name:** `azure-qlikcloud-generate-jwt-token` (choose a different name if not available)
- **Runtime stack:** Python
- **Version:** 3.11
- **Region:** Choose your region

4. Click **Review + Create**

## Install Azure CLI, Python, Azure Functions Core Tools
We will develop these functions locally, requiring Python for managing dependencies. Subsequently, we will deploy the functions to the cloud using Azure Functions Core Tools CLI. Azure CLI will handle authentication during this process.

**Download and Install these tools:**
- **Azure CLI:** 2.61 or later [Download](https://azcliprod.blob.core.windows.net/msi/azure-cli-2.61.0-x64.msi)
- **Python:** 3.11 [Download](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)
- **Azure Functions Core Tools:** 4.0 or later [Download](https://functionscdn.azureedge.net/public/artifacts/v4/latest/func-cli-x64.msi)

## Create Project Folder
1. On your local environment, create a project folder named `azure-qlikcloud-generate-jwt-token`
2. Open CMD and navigate to that folder.
3. Execute the following command:
    ```bash
    func init --python
    ```
4. Press enter. You should see the default Azure Functions files created.

## Create HTTP Trigger and Anonymous Authentication
1. Execute the following command to create a new Azure Function named `http_trigger_qlikcloud_jwt_token` using the HTTP trigger template with anonymous authentication:
    ```bash
    func new --name http_trigger_qlikcloud_jwt_token --template "HTTP trigger" --authlevel "anonymous"
    ```
2. This command initializes a new HTTP-triggered Azure Function with anonymous access authentication.

## Update requirements.txt and function_app.py Files
1. Overwrite `requirements.txt` and `function_app.py` file with these files:
    - **requirements.txt**
    - **function_app.py**

## Create a Python Virtual Environment and Install Necessary Modules
1. On CMD, execute this command to create Python Virtual Environment:
    ```bash
    python -m venv .venv
    ```
2. Activate the virtual environment using the following command (note the space at the beginning):
    ```bash
     .venv\Scripts\activate
    ```
3. Install the necessary Python modules specified in `requirements.txt` by running:
    ```bash
    pip install -r requirements.txt
    ```

## Log in to Your Azure Account Using Azure CLI
1. Hit this command:
    ```bash
    az login
    ```
2. Follow the instructions in the terminal to authenticate and complete the login process.

## Publish the Function App
1. Execute the following command to publish your Azure Function App to Azure:
    ```bash
    func azure functionapp publish your-function-name
    ```
2. Change the name with your function name, e.g., `azure-qlikcloud-generate-jwt-token`

## Set Environment Variables
1. Navigate to the Azure portal
2. In the Azure portal, locate and select your Azure Function App (`azure-qlikcloud-generate-jwt-token` in this case).
3. Create the following environment variables and add their respective values:
    - **issuer**
    - **kid**
    - **private_key**

   Here is a reference on getting the values for the variables: [Configure JWT IdP](https://docs.microsoft.com/en-us/azure/app-service/configure-authentication-provider-jwt)

## Get Function URL
1. Click on Functions: `http_trigger_qlikcloud_jwt_token`
2. In the function details page, locate the **Get function URL** option. Click on it to reveal the URL for invoking your function.

   Example: `https://azure-qlikcloud-generate-jwt-token.azurewebsites.net/api/http_trigger_qlikcloud_jwt_token_test`
3. Open the function URL in a web browser. If you receive the expected code in the response, it indicates that the function is properly configured and operational.

## Add the URL into the Embed Iframe Code Configuration
1. Go to **Embed Iframe Code:**
2. Step 3 - Configure and Embed Iframe Code into the Website
3. Change the `JWTENDPOINT` variable with Azure Function URL.

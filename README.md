# Azure Function App for Generating JWT Tokens

This Azure Function App is designed to generate JSON Web Tokens (JWT) for authentication purposes in a Qlik Cloud environment. The function is triggered via an HTTP request and generates a JWT using a private key and other environment-specific configurations.
This documentation provides a detailed overview of the code and how to set up and deploy the Azure Function App to generate JWT tokens for authentication in Qlik Cloud.

## Source and Conversion
The original script is from this [Qlik Dev documentation](https://qlik.dev/embed/iframe/quickstart/embedding-with-anonymous-access-and-qlik-cloud/#step-3---configure-web-page-variables) which uses AWS Lambda. In this guide, we convert the implementation into an Azure Function App.

## Create Azure Functions App
1. Go to [Azure Portal](https://portal.azure.com/#create/Microsoft.FunctionApp)
2. Select **Consumption** for the hosting plan.
3. Enter your **Subscription** and **Resource Group**. Create a new one if you don’t have any.

**Configuration:**
- **Function App name:** `azure-qlikcloud-generate-jwt-token` (choose a different name if not available)
- **Runtime stack:** Python
- **Version:** 3.11
- **Region:** Choose your region

4. Click **Review + Create**, then click **Create** to finalize.

## Set Environment Variables
1. Navigate to the Azure portal.
2. Locate and select your Azure Function App (`azure-qlikcloud-generate-jwt-token` in this case).
3. In the Function App, go to **Configuration** under the **Settings** section.
4. Add the following environment variables:
   - **AzureWebJobsStorage**: Obtain the connection string from your Azure Storage account.
      - On Azure Portal, open the storage account you want to obtain the connection string for. Select Access keys under the Security + networking section.
      - You will see two access keys (Key1 and Key2) and the corresponding connection strings for your storage account. Please use any connection string field associated with either Key1 or Key2.
   - **issuer**
   - **kid**
   - **private_key**

   For guidance on obtaining the values for `issuer`, `kid`, and `private_key`, refer to [Configure JWT IdP](https://qlik.dev/embed/iframe/quickstart/embedding-with-anonymous-access-and-qlik-cloud/).

## Install Azure CLI and Azure Functions Core Tools
We will deploy the functions to the cloud using Azure Functions Core Tools CLI. Azure CLI will handle authentication during this process.

**Download and Install these tools:**
- **Azure CLI:** 2.61 or later [Download](https://azcliprod.blob.core.windows.net/msi/azure-cli-2.61.0-x64.msi)
- **Azure Functions Core Tools:** 4.0 or later [Download](https://functionscdn.azureedge.net/public/artifacts/v4/latest/func-cli-x64.msi)

## Download and Unzip the Package
1. Download the package and unzip it.
2. Open CMD and navigate to the folder. Use the command: `cd path_to_unzipped_folder/azure-qlikcloud-generate-jwt-token`

## Log in to Your Azure Account Using Azure CLI
1. Execute the following command to log in:
    ```bash
    az login
    ```
2. Follow the instructions in the terminal to authenticate and complete the login process.

## Publish the Function App
1. Execute the following command to publish your Azure Function App to Azure:
    ```bash
    func azure functionapp publish azure-qlikcloud-generate-jwt-token
    ```
2. Replace `azure-qlikcloud-generate-jwt-token` with your function name if it's different.

## Get Function URL
1. In the Azure portal, go to your Function App.
2. Click on the function: `http_trigger_qlikcloud_jwt_token`.
3. On the function details page, locate the **Get function URL** option. Click on it to reveal the URL for invoking your function.

   Example: `https://azure-qlikcloud-generate-jwt-token.azurewebsites.net/api/http_trigger_qlikcloud_jwt_token`
4. Open the function URL in a web browser. If you receive the expected response, it indicates that the function is properly configured and operational.
   ```bash
   {
       "body": "eyJhbGciOiJ..."
   }
    ```
## Add the URL into the Embed Iframe Code Configuration
1. Go to the **Embed Iframe Code** section of your application.
2. In [Step 3 - Configure and Embed Iframe Code into the Website](https://qlik.dev/embed/iframe/quickstart/embedding-with-anonymous-access-and-qlik-cloud/#step-3---configure-web-page-variables), update the `JWTENDPOINT` variable with the Azure Function URL obtained in the previous step.

This completes the setup and deployment of your Azure Function App for generating JWT tokens.

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

# Initialize Azure Key Vault Client
vault_url = os.getenv("AZURE_KEYVAULT_URL")
credential = DefaultAzureCredential()
client = SecretClient(vault_url=vault_url, credential=credential)

def get_secret(key):
    try:
        secret = client.get_secret(key)
        return secret.value
    except Exception as e:
        return f"Error retrieving secret: {str(e)}"

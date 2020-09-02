from azure.identity import ClientSecretCredential
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


class AzureVault:
    
    def add_secret(self):
        """
        Responsible to ADD secrets in Azure Vault.
        ref.: https://pypi.org/project/azure-keyvault-secrets/#set-a-secret
        """
        credential = DefaultAzureCredential()
        # credential = ClientSecretCredential(tenant_id, client_id, client_secret)

        secret_client = SecretClient(vault_url="https://my-key-vault.vault.azure.net/", credential=credential)
        secret = secret_client.set_secret("secret-name", "secret-value")

        print(secret.name)
        print(secret.value)
        print(secret.properties.version)

    def delete_secret(self):
        """
        Responsible to DELETE secrets in vault.
        ref.: https://pypi.org/project/azure-keyvault-secrets/#delete-a-secret
        """
        credential = DefaultAzureCredential()

        secret_client = SecretClient(vault_url="https://my-key-vault.vault.azure.net/", credential=credential)
        deleted_secret = secret_client.begin_delete_secret("secret-name").result()

        print(deleted_secret.name)
        print(deleted_secret.deleted_date)

    def get_secret(self):
        """
        Responsible to RETRIEVE secrets from Vault.
        ref.: https://pypi.org/project/azure-keyvault-secrets/#retrieve-a-secret
        """
        credential = DefaultAzureCredential()

        secret_client = SecretClient(vault_url="https://my-key-vault.vault.azure.net/", credential=credential)
        secret = secret_client.get_secret("secret-name")

        print(secret.name)
        print(secret.value)

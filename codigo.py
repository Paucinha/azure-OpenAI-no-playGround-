  
import os  
import base64
from openai import AzureOpenAI  
from azure.identity import DefaultAzureCredential, get_bearer_token_provider  
        
endpoint = os.getenv("ENDPOINT_URL", "https://pauci-m7r4nsxv-northcentralus.openai.azure.com/")  
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo-16k")  
      
# Inicializar o cliente do Serviço OpenAI do Azure com autenticação do Entra ID
token_provider = get_bearer_token_provider(  
    DefaultAzureCredential(),  
    "https://cognitiveservices.azure.com/.default"  
)  
  
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    azure_ad_token_provider=token_provider,  
    api_version="2024-05-01-preview",  
)  
  

chat_prompt = [
    {
        "role": "system",
        "content": "Você é um assistente de IA que ajuda as pessoas a encontrar informações."
    }
] 
    
# Incluir resultado de fala se a fala estiver habilitada  
messages = chat_prompt 

completion = client.chat.completions.create(  
    model=deployment,  
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False  
)  
  
print(completion.to_json())
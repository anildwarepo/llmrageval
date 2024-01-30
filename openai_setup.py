from dotenv import load_dotenv
from pathlib import Path 
import os
import openai

env_path = Path('.') / 'secrets.env'
load_dotenv(dotenv_path=env_path)


print(f'AZURE_OPENAI_ENDPOINT:{os.environ["AZURE_OPENAI_ENDPOINT"]}')



# Configure the baseline configuration of the OpenAI library for Azure OpenAI Service.
#OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
#OPENAI_DEPLOYMENT_NAME = os.environ["DEPLOYMENT_NAME"]
openai.api_type = "azure"
openai.api_base = os.environ["AZURE_OPENAI_ENDPOINT"]
openai.api_version = os.environ["OPENAI_API_VERSION"]
openai.api_key = os.environ["AZURE_OPENAI_API_KEY"]
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("ENDPOINT")
    KEY = os.getenv("SUBSCRIPTION_KEY")
    LOCATION = os.getenv("LOCATION")
    TARGET_LANGUAGE = "pt-br"

    OAI_ENDPOINT = os.getenv("OAI_ENDPOINT")
    OAI_KEY = os.getenv("OAI_KEY")
    OAI_LOCATION = os.getenv("OAI_LOCATION")
    OAI_VERSION = os.getenv("OAI_API_VERSION")
    OAI_DEPLOYMENT_NAME = os.getenv("OAI_DEPLOYMENT_NAME")
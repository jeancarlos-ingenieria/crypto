import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    return os.getenv("CMC_API_KEY")

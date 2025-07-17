from dotenv import load_dotenv
import os

def env():
    load_dotenv(override=True)

    api_key = os.getenv("API_KEY")

    numeros = list(map(int, os.getenv('NUMEROS').split(',')))

    return api_key, numeros
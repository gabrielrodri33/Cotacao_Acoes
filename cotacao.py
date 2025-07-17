from dotenv import load_dotenv
from io import StringIO
import os
import requests
import pandas as pd
import csv
import json
import yfinance as yf

def env():
    load_dotenv(override=True)

    phone = list(map(int, os.getenv('NUMEROS').split(',')))

    return phone

def cotacao_acao():
    acoes = ["MXRF11.SA", "BBAS3.SA", "TAEE4.SA"]

    for acao in acoes:
        dado = yf.Ticker(acao)
        info = dado.info

        print(json.dumps(info, indent=4, ensure_ascii=False))

        print(f"\n📈 {acao}")
        print(f"Preço atual: R$ {info.get('currentPrice')}")
        print(f"Abertura: R${info.get('open')}")
        print(f"Prévia de fechamento: R${info.get('previousClose')}")
        print(f"Máxima diária: R$ {info.get('dayHigh')}")
        print(f"Mínima diária: R$ {info.get('dayLow')}")

def main():
    cotacao_acao()

if __name__ == "__main__":
    main()

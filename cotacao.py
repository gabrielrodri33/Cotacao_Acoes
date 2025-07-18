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
        info = yf.Ticker(acao).info

        # print(json.dumps(info, indent=4, ensure_ascii=False))

        print(f"\n📈 {acao}")
        print(f"Preço atual: R$ {info.get('currentPrice'):.2f}")
        print(f"Abertura: R${info.get('open'):.2f}")
        print(f"Prévia de fechamento: R${info.get('previousClose'):.2f}")
        print(f"Máxima diária: R$ {info.get('dayHigh'):.2f}")
        print(f"Mínima diária: R$ {info.get('dayLow'):.2f}")

def cotacao_cripto():
    criptos = ["BTC-USD", "USDC-USD", "ETH-USD"]

    cotacao_dolar = yf.Ticker("USDBRL=X").info.get("regularMarketPrice")

    for cripto in criptos:
        info = yf.Ticker(cripto).info

        # print(json.dumps(info, indent=4, ensure_ascii=False))
        
        preco_brl = info.get("regularMarketPrice", 0) * cotacao_dolar

        print(f"\n💰 {cripto} em US$")
        print(f"Preço atual: R$ {preco_brl:.2f}")
        print(f"Máxima diária: R$ {info.get('dayHigh', 0) *cotacao_dolar:.2f}")
        print(f"Mínima diária: R$ {info.get('dayLow', 0) * cotacao_dolar:.2f}")

def main():
    cotacao_acao()
    cotacao_cripto()

if __name__ == "__main__":
    main()

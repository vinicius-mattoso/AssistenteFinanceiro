import yfinance as yf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import json
import os

def retorna_cotacao(ticker, periodo="1y"):
    ticker_obj = yf.Ticker(f"{ticker}.SA")
    hist = ticker_obj.history(period=periodo)

    if hist.empty or "Close" not in hist.columns:
        return json.dumps({
            "erro": "Não foi possível recuperar os dados para o ticker informado."
        })

    hist["Data"] = hist.index.strftime("%Y-%m-%d")
    hist["Close"] = round(hist["Close"], 2)

    # Últimos 12 registros de fechamento
    ultimos_12 = hist["Close"].tail(12)

    # Informações estatísticas
    valor_min = float(hist["Close"].min())
    valor_max = float(hist["Close"].max())
    valor_ultimo = float(hist["Close"].iloc[-1])
    valor_medio = round(hist["Close"].mean(), 2)

    # Gráfico 1: Preço simples
    plt.figure(figsize=(10, 5))
    plt.plot(ultimos_12.index, ultimos_12.values, marker='o', linestyle='-', color='royalblue', linewidth=2)
    plt.title(f"Cotação de {ticker.upper()} - Últimos 12 registros", fontsize=14)
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    data_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo1 = f"assets/grafico_{ticker.lower()}_{data_str}.svg"
    plt.savefig(nome_arquivo1, format='svg')
    plt.close()

    # -----------------------------------------
    # Gráfico 2: Bollinger Bands + Médias móveis
    # -----------------------------------------

    df = hist.copy()
    df["MM_20"] = df["Close"].rolling(window=20).mean()
    df["STD_20"] = df["Close"].rolling(window=20).std()
    df["Banda_Sup"] = df["MM_20"] + 2 * df["STD_20"]
    df["Banda_Inf"] = df["MM_20"] - 2 * df["STD_20"]

    df["MM_40"] = df["Close"].rolling(window=40).mean()
    df["MM_60"] = df["Close"].rolling(window=60).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(df["Data"], df["Close"], label="Preço Fechamento", color="black", linewidth=1.5)
    plt.plot(df["Data"], df["MM_20"], label="Média Móvel 20 dias", linestyle="--", color="blue")
    plt.plot(df["Data"], df["Banda_Sup"], label="Banda Superior", linestyle=":", color="red")
    plt.plot(df["Data"], df["Banda_Inf"], label="Banda Inferior", linestyle=":", color="green")
    plt.plot(df["Data"], df["MM_40"], label="MM 2 meses", linestyle="-.", color="purple")
    plt.plot(df["Data"], df["MM_60"], label="MM 3 meses", linestyle="-.", color="orange")

    plt.fill_between(df["Data"], df["Banda_Inf"], df["Banda_Sup"], color='gray', alpha=0.1)
    plt.legend()
    plt.title(f"Bandas de Bollinger e  Médias móveis - {ticker.upper()}", fontsize=14)
    plt.xlabel("Data")
    plt.ylabel("Preço (R$)")
    plt.xticks(rotation=45)
    ticks_to_show = df["Data"].iloc[::max(1, len(df)//12)]
    plt.xticks(ticks_to_show, rotation=45)
    plt.tight_layout()
    nome_arquivo2 = f"assets/grafico_bollinger_{ticker.lower()}_{data_str}.svg"
    plt.savefig(nome_arquivo2, format='svg')
    plt.close()

    # return json.dumps({
    #     "dados_historicos": df[["Data", "Close"]].tail(30).to_dict(orient="records"),
    #     "valor_minimo": valor_min,
    #     "valor_maximo": valor_max,
    #     "valor_medio": valor_medio,
    #     "valor_ultimo": valor_ultimo,
    #     "ultimos_12_valores": ultimos_12.to_dict(),
    #     "grafico_nome_arquivo": os.path.basename(nome_arquivo1),
    #     "grafico_bollinger": os.path.basename(nome_arquivo2)
    # })
    return json.dumps({
        "dados_historicos": [
            {"data": str(k), "valor": float(v)}
            for k, v in hist["Close"].tail(30).items()
        ],
        "valor_minimo": valor_min,
        "valor_maximo": valor_max,
        "valor_medio": valor_medio,
        "valor_ultimo": valor_ultimo,
        "ultimos_12_valores": {str(k): v for k, v in ultimos_12.items()},
        "grafico_nome_arquivo": os.path.basename(nome_arquivo1),
        "grafico_bollinger": os.path.basename(nome_arquivo2)
    })

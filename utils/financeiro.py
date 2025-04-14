import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import json

def retorna_cotacao(ticker, periodo="1y"):
    ticker_obj = yf.Ticker(f"{ticker}.SA")
    hist = ticker_obj.history(period=periodo)["Close"]

    if hist.empty:
        return {
            "erro": "Não foi possível recuperar os dados para o ticker informado."
        }

    hist.index = hist.index.strftime("%Y-%m-%d")
    hist = round(hist, 2)

    valor_min = float(hist.min())
    valor_max = float(hist.max())
    valor_ultimo = float(hist.iloc[-1])
    valor_medio = round(hist.mean(), 2)

    ultimos_12 = hist.tail(12)

    # Gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(ultimos_12.index, ultimos_12.values, marker='o', color='royalblue')
    plt.title(f"Cotação média de {ticker.upper()} - Últimos 12 registros")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    data_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"assets/grafico_{ticker.lower()}_{data_str}.svg"
    plt.savefig(nome_arquivo, format='svg')
    plt.close()

    return {
        "dados_historicos": hist.tail(30).to_dict(),
        "valor_minimo": valor_min,
        "valor_maximo": valor_max,
        "valor_medio": valor_medio,
        "valor_ultimo": valor_ultimo,
        "ultimos_12_valores": ultimos_12.to_dict(),
        "grafico_salvo_em": nome_arquivo
    }

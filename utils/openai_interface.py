import openai
import json
from utils.financeiro import retorna_cotacao
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env
client = openai.Client(api_key=os.getenv("OPENAI_API_KEY"))

def consultar_chatgpt(pergunta):
    ferramentas = [{
        "type": "function",
        "function": {
            "name": "retorna_cotacao",
            "description": "Retorna a cotação de ações da Ibovespa e gera gráfico",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Ticker da ação. Ex: BBAS3, PETR4, etc."
                    },
                    "periodo": {
                        "type": "string",
                        "enum": ["1d", "5d", "1mo", "6mo", "1y", "5y", "10y", "ytd", "max"]
                    }
                }
            }
        }
    }]

    mensagens = [{"role": "user", "content": pergunta}]
    resposta = client.chat.completions.create(
        messages=mensagens,
        model="gpt-3.5-turbo-0125",
        tools=ferramentas,
        tool_choice="auto"
    )

    tool_calls = resposta.choices[0].message.tool_calls
    if not tool_calls:
        return {"resposta": resposta.choices[0].message.content, "grafico_salvo_em": None}

    mensagens.append(resposta.choices[0].message)

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        resultado = retorna_cotacao(**function_args)

        mensagens.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": function_name,
            "content": json.dumps(resultado)
        })

        segunda_resposta = client.chat.completions.create(
            messages=mensagens,
            model="gpt-3.5-turbo-0125"
        )
        mensagem_final = segunda_resposta.choices[0].message.content
        mensagem_sem_link = mensagem_final.split("![")[0].strip()
        return {
            "resposta": mensagem_sem_link,
            "grafico_salvo_em": resultado.get("grafico_salvo_em")
        }

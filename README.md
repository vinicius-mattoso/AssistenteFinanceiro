# 💰 Assistente Financeiro com Dash + OpenAI

Um assistente inteligente para auxiliar na análise de ações da bolsa de valores brasileira (B3), utilizando **Dash multipage**, **gráficos interativos com Matplotlib**, integração com **OpenAI** (ChatGPT) e dados reais via **Yahoo Finance**.

---

## 🧠 Sobre o projeto

O objetivo é oferecer uma interface intuitiva onde o usuário pode perguntar, por exemplo:

> *"Como estão as ações do Banco do Brasil nos últimos 12 meses?"*

A IA responde com uma análise resumida, enquanto o sistema gera automaticamente:

- Um gráfico com os preços de fechamento dos últimos dias.
- Um gráfico com **Bandas de Bollinger** e **Médias móveis** de 2 e 3 meses.

---

## ⚙️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Dash](https://dash.plotly.com/)
- [Plotly](https://plotly.com/python/)
- [Matplotlib](https://matplotlib.org/)
- [OpenAI GPT (API)](https://platform.openai.com/)
- [yFinance](https://pypi.org/project/yfinance/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## ▶️ Como executar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/assistente-financeiro.git
cd assistente-financeiro
```

2. **Crie um ambiente virtual e ative-o:**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure a variável de ambiente:**

Crie um arquivo .env na raiz do projeto:
```bash
OPENAI_API_KEY=sua-chave-aqui
```

5. **Execute o app:**

```bash
python app.py
```

## 📁 Estrutura do projeto
```bash
assistente_financeiro/
│
├── app.py                    # Arquivo principal da aplicação
├── assets/                   # Arquivos estáticos (.svg, estilos)
│   └── style.css
│   └── logo and icons
├── pages/                    # Páginas do Dash (home, assistente)
│   ├── home.py
│   └── assistente.py
├── components/               # Componentes reutilizáveis (navbar)
│   └── navbar.py
├── utils/                    # Funções auxiliares e integração OpenAI
│   ├── financeiro.py
│   └── openai_interface.py
├── .env                      # (não versionado) Chave da OpenAI
└── README.md
```

✅ Funcionalidades atuais
* Página inicial com introdução ao projeto

* Página "Assistente" com campo de pergunta e botão "Consultar"

* Conexão com a OpenAI via função tool_call

* Geração de gráficos:

* Preço de fechamento médio dos últimos 12 registros

* Bandas de Bollinger + Médias móveis (2 e 3 meses)


## 🧩 Ideias de melhorias futuras

- [ ] ✅ Botão "Limpar Pesquisa" para apagar gráficos e limpar interface  
- [ ] 📊 Gráficos interativos com Plotly (em vez de Matplotlib)  
- [ ] 📤 Exportar análise como PDF    
- [ ] 📈 Adicionar outros indicadores técnicos
- [ ] 📈 Criar um docker da aplicação
- [ ] ☁️ Deploy na nuvem (Render, Vercel, Heroku, etc)
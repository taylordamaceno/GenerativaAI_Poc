import json
import openai

# Carregar os dados financeiros do arquivo JSON
with open("financeirorelatorio.json", "r") as f:
    financial_data = json.load(f)

# Converter os dados financeiros para uma string formatada
financial_data_str = "\n".join([f"{key}: {value}" for key, value in financial_data.items()])

# Obter a chave da API do vault
with open("vault.json", "r") as f:
    data = json.load(f)
    api_key = data["api_key"]

# Configurar a chave da API
openai.api_key = api_key

# Fazer a chamada à API para gerar um resumo executivo
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=f"crie um relatório financeiro em forma de texto na lingua portuguesa(br)  que análise de forma critica e propositiva os numeros que estou disponibilizando propondo algumas acoes para melhoria  based on the following financial data:\n{financial_data_str}",
  max_tokens=3000
)

# Exibir o resumo gerado
with open("resumoexecutivo.txt", "w") as f:
    f.write(response.choices[0].text.strip())

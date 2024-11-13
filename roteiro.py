import os
import yaml
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt
import ast  


with open('roteiro.yaml', 'r') as file:
    roteiro_data = yaml.safe_load(file)

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


turismo_data = []

# Executar os prompts para cada cidade e estruturar a resposta como JSON
for cidade, info in roteiro_data['roteiro'].items():
    prompt = f"{info['prompt']} Responda no formato JSON com os campos: 'nome', 'descrição', e 'visitantes'."
    print(f"\nExecutando prompt para {cidade.capitalize()}...")

    # Gerar o conteúdo com o prompt do YAML
    response = model.generate_content(prompt)
    result_json = response.text
    
    # Remover delimitadores de código se existirem
    result_json = result_json.strip('```json').strip('```').strip()

    # Avaliar o JSON de forma segura e adicionar a cidade para cada ponto turístico
    try:
        pontos = ast.literal_eval(result_json) 
        for ponto in pontos:
            ponto['cidade'] = cidade.capitalize()
            turismo_data.append(ponto)
    except Exception as e:
        print(f"Erro ao avaliar o JSON para {cidade.capitalize()}: {e}")

df = pd.DataFrame(turismo_data)

def convert_to_int(value):
    try:
        value = str(value).lower().replace(",", "").replace(".", "").strip()  
        if "milhão" in value:
            return int(float(value.split()[0]) * 1_000_000)
        elif "mil" in value:
            return int(float(value.split()[0]) * 1_000)
        else:
            return int(value)
    except (ValueError, IndexError):
        print(f"Valor inválido para conversão: {value}")
        return 0 

df['visitantes'] = df['visitantes'].apply(convert_to_int)
df = df.sort_values('visitantes', ascending=True)  



#Elaboração Gráfico
colors = {'Atenas': 'skyblue', 'Roma': 'salmon'}
df['color'] = df['cidade'].map(colors)  


plt.figure(figsize=(10, 8))
plt.barh(df['nome'], df['visitantes'], color=df['color'])
plt.xlabel('Número Anual de Visitantes')
plt.ylabel('Pontos Turísticos')
plt.title('Número Anual de Visitantes dos Pontos Turísticos em Atenas e Roma')


for cidade, color in colors.items():
    plt.barh([], [], color=color, label=cidade)
plt.legend(title='Cidade')


plt.show()







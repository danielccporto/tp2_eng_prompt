
import os
from dotenv import load_dotenv
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

# Atividade 7
#response = model.generate_content("""Quero que você faça um resumo da notícia que irei incluir a seguir.Retorno 
#os principais envolvidos, localidade, data e o que aconteceu na notícia. 
#Notícia:  Polícia suspeita que PCC monitorou voo de delator executado em SP e vai analisar lista de passageiros
#Suspeita com base em informações de inteligência é de que facção criminosa vinha monitorando os passos de 
#Vinicius Gritzbach na capital alagoana e no trajeto de volta a São Paulo. Ele foi morto na sexta-feira no 
#desembarque do aeroporto de Guarulhos.""")
#print(response.text)

#Atividade 8 
response = model.generate_content("""Com base em três notícias que irei enviar, irei seus recursos 
para que você encontre possíveis envolvidos nas notícias em questão. Pode ser uma resposta objetiva,
em tom jornalistico e quero que você encontre possíveis pessoas, órgãos públicos, empresas ou 
qualquer tipo de envolvidos na mesma, citando quem são os envolvidos e qual tipo 
de envolvidos estamos falando. Não preciso de informações extras. 
                                  
Notícia 1: Trump confirma Elon Musk no Departamento de Eficiência Governamental para cortar gastos
Bilionário dono da Tesla irá trabalhar em conjunto com Vivek Ramaswamy, que disputou as primárias 
republicanas para concorrer à presidência. Anúncio foi feito na noite desta terça-feira (12).
                                  
Notícia 2: Flamengo afasta Gabigol do jogo contra o Atlético-MG; atacante promete à torcida: "Estaremos juntos na Norte"
Clube comunica que terá reunião com representantes do atleta para definir os próximos passos
                                  
Notícia 3: Lula encontra Pacheco e senadores nesta quarta e pode apresentar pacote de corte de gastos
Planalto quer mostrar propostas à cúpula do Congresso antes de divulgar pacote; reunião não consta 
na agenda de Lula. Lira disse ao g1 que não recebeu 'nenhum convite'.
""")
print(response.text)




"""
#Desafio1: Circunferencia 
#Dada a equacao da circunferencia faca o grafico
#(x-a)² + (y-b)² = r²
import math
import matplotlib.pyplot as plt

r = 100
a = 100
b= 100
x= []
y= []

x = [ i for i in range(2*r+1)]
y_x = lambda x: b + math.sqrt(r**2 - (x-a)**2)
y_x_neg = lambda x: b - math.sqrt(r**2 - (x-a)**2)

y.extend(list(map(y_x, x)))
y.extend(list(map(y_x_neg, x)))
x.extend(list(reversed(x)))

plt.plot(x, y, color='blue')
print(f"Coordenadas da circunferencia: {list(zip(x, y))}")
print(plt.show())


#Desafio2: Como ler arquivos .txt e csv.
file_path = 'Testes.txt'  # Substitua pelo caminho do seu arquivo .txt

with open(file_path, 'r') as file:
    content = file.read()
    print("Conteúdo do arquivo .txt:")
    print(content)

lista_colunas = content.split('\n')[0].strip().split(',')  # Obtendo os nomes das colunas
print("Nomes das colunas do arquivo .csv:")

#Desafio3: Importar a tabela dos 100 maiores municipios em relação ao IBGE e responder as seguintes perguntas:
#Quantos municipios estão nos estado de São Paulo?
#Qual a participação acumulada desses municipios em relação ao PIB do Brasil??

file_path = 'PIB_Municípios.txt'

# Lê o arquivo dividindo diretamente em linhas
with open(file_path, 'r', encoding='latin-1') as file:
    linhas = [line.strip().split(',') for line in file.readlines()]

# O cabeçalho está na primeira linha
cabecalho = linhas[0]

# Inicializa o dicionário para cada coluna do cabeçalho
colunas_dict = {coluna: [] for coluna in cabecalho}

# Identifica o índice da coluna 'Estados'
indice_estado = cabecalho.index('Estados')

# Preenche o dicionário com os dados das linhas seguintes
for linha in linhas[1:]:
    # Garante que a linha tem o mesmo número de colunas para evitar erros de índice
    if len(linha) == len(cabecalho):
        for i, coluna in enumerate(cabecalho):
            colunas_dict[coluna].append(linha[i])

print(colunas_dict['Estados'])

import pandas as pd 

dict_data = {'coluna_a': [1,2,3], 'coluna_2': [4,5,6]}

df_data = pd.DataFrame(dict_data)
print(df_data.head(2)) #Serve para otimizar colunas. 

"""




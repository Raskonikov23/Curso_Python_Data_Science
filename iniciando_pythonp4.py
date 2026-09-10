"""
#Exercicio3: Criar o modulo que receba o peso e altura e calcule o IMC e retorne a classificação do IMC.

peso = float(input("Digite o seu peso em kg: "))

altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"

elif imc < 25:
    classificacao = "Peso normal"

elif imc < 30:
    classificacao = "Sobrepeso"

elif imc < 35:
    classificacao = "Obesidade grau I"

elif imc < 40:
    classificacao = "Obesidade grau II"

else:
    classificacao = "Obesidade grau III"

print(f"Seu IMC é: {imc:.2f} e sua classificação é: {classificacao}")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
z = [3, 4, 5, 6, 7]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 

ax.scatter(x, y, z)

plt.title("Gráfico 3D de Dispersão")
plt.show()

#Desafio1: Criar um modulo que leia um arquivo de pontos 3D e faça um gráfico desses pontos. 


file_name = 'pontos_esfera.txt'


def coord_esfera(file_name):

    with open(file_name, 'r') as f:
        f_data = f.readlines()

    linha = []

    # Ignora a primeira linha (x y z)
    for i in range(1, len(f_data)):
        linha.append(f_data[i].strip().split())

    coordenadas = {}

    coordenadas['x'] = []
    coordenadas['y'] = []
    coordenadas['z'] = []

    for i in range(len(linha)):
        coordenadas['x'].append(float(linha[i][0]))
        coordenadas['y'].append(float(linha[i][1]))
        coordenadas['z'].append(float(linha[i][2]))

    coordenadas['x'] = tuple(coordenadas['x'])
    coordenadas['y'] = tuple(coordenadas['y'])
    coordenadas['z'] = tuple(coordenadas['z'])

    return coordenadas


def plot_3d(coordenadas):

    import matplotlib.pyplot as plt

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(
        coordenadas['x'],
        coordenadas['y'],
        coordenadas['z']
    )

    plt.title("Gráfico 3D de Dispersão")

    plt.show()


coordenadas = coord_esfera(file_name)

plot_3d(coordenadas)

#Noçoes de Objetos 

class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.dono = []
    def add_dono(self, nome):
        self.dono.append(nome)  
        

meu_carro = carro("Toyota", "Corolla", 2020)

print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Ano: {meu_carro.ano}")
print(f"Dono(s): {meu_carro.dono}")
"""
class vetor_2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
v_1 = vetor_2d(3, 3)
v_2 = vetor_2d(4, 4)

v_3 = vetor_2d(v_1.x + v_2.x, v_1.y + v_2.y)
print(f"Vetor resultante: ({v_3.x}, {v_3.y})")
"""
#Executando Modulos como scripts
#Modulos como scripts podem ser executados diretamente, mas tambem podem ser importados como modulos em outros scripts.
#São importantes para organizar o código e reutilizar funções e classes em diferentes partes de um projeto.
#São bastante utilizados em projetos maiores, onde o código é dividido em diferentes arquivos para facilitar a manutenção e a colaboração 
# entre desenvolvedores.


def funcao1():
    print("Função 1 executada")
def funcao2():
    print("Função 2 executada")
if __name__ == '__main__':
    funcao1()
    funcao2()

#Manipulando Strings
#Strings são sequências de caracteres que podem ser manipuladas de diversas formas em Python.
# Elas podem ser criadas utilizando aspas simples (' ') ou aspas duplas (" ").
# Algumas operações comuns com strings incluem: upper(), lower(), strip(), replace(), split(), join(), find(), len(), entre outras.

string1 = "Olá, mundo!"
string2 = string1.upper()  # Converte para maiúsculas
string3 = string1.lower()  # Converte para minúsculas
string4 = string1.strip()  # Remove espaços em branco no início e no fim
string5 = string1.replace("mundo", "Python")  # Substitui "mundo" por "Python"
string6 = string1.split(",")  # Divide a string em uma lista usando a vírgula como separador
string7 = "-".join(string6)  # Junta a lista em uma string usando o hífen como separador
string8 = string1.find("mundo")  # Encontra a posição da substring "mundo"
string9 = len(string1)  # Obtém o comprimento da string
print(string1)
print(string2)
print(string3)
print(string4)
print(string5)
print(string6)
print(string7)
print(string8)
print(string9)

#Escrevendo Arquivos 
#Escrever arquivos em Python é uma tarefa comum, e pode ser feita utilizando a função open() com o modo de escrita ('w') ou adição ('a').
# O modo 'w' cria um novo arquivo ou sobrescreve um arquivo existente, enquanto o modo 'a' adiciona conteúdo ao final de um arquivo existente.

with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Escrevendo em um arquivo de texto.\n")
    arquivo.write("Python é incrível!\n")
print("Arquivo escrito com sucesso!")

#Graficos, onde procurar e como aprender. 
# A função linspace do NumPy é usada para criar um array de números igualmente espaçados entre dois valores especificados.
# A função linspace é útil para gerar pontos de dados para gráficos, simulações e outras aplicações que requerem uma distribuição uniforme 
# de valores.
# Os gráficos são feitos de acordo com a necessidade, por isso é importante ir no site e pesquisar mais sobre o assunto, existem diversos
#  tipos de gráficos e cada um tem sua função específica.
# A função arange do NumPy é usada para criar um array de números igualmente espaçados dentro de um intervalo especificado.
# A função set do Matplotlib é usada para definir propriedades de um objeto, como rótulos, títulos e limites de eixos em gráficos.

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(1.0, 2.0, 0.05)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='Nome que pode se dar ao gráfico')
ax.grid()

fig.savefig("test.png")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-t))

fig, ax = plt.subplots()
ax.axhline(y=0, color="black", linestyle="--")
ax.axhline(y=0.5, color="black", linestyle=":")
ax.axhline(y=1.0, color="black", linestyle="--")
ax.axvline(color="grey")
ax.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))
ax.plot(t, sig, linewidth=2, label=r"$\sigma(t) = \frac{1}{1 + e^{-t}}$")
ax.set(xlim=(-10, 10), xlabel="t")
ax.legend(fontsize=14)
plt.show()

"""
# Como Automatizar tarefas com Python
# Automatizar tarefas com Python é uma maneira eficiente de economizar tempo e reduzir erros em processos repetitivos.
#  Python oferece diversas bibliotecas e ferramentas que permitem automatizar tarefas em diferentes áreas, como web scraping, 
# manipulação de arquivos, envio de e-mails, entre outras.
# Essa seção vai muito do dia a dia, e é importante ir pesquisando e aprendendo mais sobre o assunto, existem diversos 
# tipos de automações que podem ser feitas com Python, vai de acordo com a necessidade de cada um, e é importante ir 
# pesquisando e aprendendo mais sobre o assunto.
"""
Método para listas. 
.appende(vatrialvel) Adiciona a variavel no final da lista.
.extend(lista) Adiciona os elementos da lista no final da lista.
.remove(valor) Remove o valor da lista.
.count(valor) Conta quantas vezes o valor aparece na lista.
.sort() Ordena a lista.
.reverse() Inverte a lista.
.copy() Cria uma cópia da lista.
.index(valor) Retorna o índice do valor na lista.

lista_inteiros = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista_inteiros.append(lista2) # Adiciona a lista2 no final da lista_inteiros
print(lista_inteiros) # Saída: [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]

lista_letras = ['a', 'b', 'c', 'd', 'e']
n_vezes = lista_letras.count('') # Conta quantas vezes a letra 'a' aparece na lista_letras
print(n_vezes) # Saída: 0

lista_3 = [3, 1, 4, 2, 5]
lista_3.sort() # Ordena a lista_3
print(lista_3) # Saída: [1, 2, 3, 4, 5]

lista_quadrados = [ ]
for i in range(5):
    lista_quadrados.append(i ** 2)
print(lista_quadrados) # Saída: [0, 1, 4, 9, 16]

# função lambda é uma função anônima, ou seja, uma função sem nome. Ela é utilizada para criar funções simples e rápidas, geralmente em uma única linha de código.

numeros = [1, 2, 3, 4, 5]
# Função lambda que retorna o quadrado de um número
f = lambda x:x**2
# Utilizando a função lambda para calcular o quadrado de cada número da lista
print(list(map(f, numeros))) # Saída: [1, 4, 9, 16, 25]
#map é uma função que aplica uma função a cada item de um iterável (como uma lista) e retorna um iterador com os resultados. 
# No exemplo acima, a função lambda é aplicada a cada número da lista "numeros", retornando uma nova lista com os quadrados desses números.


#Tuplas, Conjuntos e Dicionários
#Tuplas são estruturas de dados que armazenam uma coleção de elementos, assim como listas, mas diferentemente delas, as tuplas são imutáveis, ou seja, não podem ser alteradas após a sua criação. Elas são definidas utilizando parênteses ().
vogais = ('a', 'e', 'i', 'o', 'u')
#Conjuntos são estruturas de dados que armazenam uma coleção de elementos únicos, ou seja, não permitem elementos duplicados. Eles são definidos utilizando chaves {}.
vogais = [0]
print(len(vogais)) # Saída: {0}

for i in enumerate(vogais):
    print(type(i)) # Saída: (0, 0)

# .items() é um método que retorna uma lista de tuplas, onde cada tupla contém um par chave-valor do dicionário. Ele é utilizado para iterar sobre os itens de um dicionário.
dicionario = {'a': 1, 'b': 2, 'c': 3}
for chave, valor in dicionario.items():
    print(chave, valor) # Saída: a 1, b 2, c 3

#.keys() é um método que retorna uma lista com todas as chaves do dicionário. Ele é utilizado para iterar sobre as chaves de um dicionário.
for chave in dicionario.keys():
    print(chave) # Saída: a, b, c

#.values() é um método que retorna uma lista com todos os valores do dicionário. Ele é utilizado para iterar sobre os valores de um dicionário.
for valor in dicionario.values():
    print(valor) # Saída: 1, 2, 3

#.pop(key) é um método que remove o item com a chave especificada do dicionário e retorna o valor correspondente. Se a chave não existir, ele gera um erro.
valor_removido = dicionario.pop('b')
print(valor_removido) # Saída: 2
print(dicionario) # Saída: {'a': 1, 'c': 3}

#.copy() é um método que cria uma cópia rasa (shallow copy) do dicionário. Ele é utilizado para criar uma nova instância do dicionário com os mesmos itens.
dicionario_copia = dicionario.copy()   

#.clear() é um método que remove todos os itens do dicionário, deixando-o vazio. Ele é utilizado para limpar o conteúdo do dicionário.
dicionario.clear()

#Métodos para Dicionários

alg_romanos = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
print(alg_romanos) # Saída: {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}

list(alg_romanos.keys()) # Saída: ['I', 'II', 'III', 'IV', 'V'] 
alg_romanos.values() # Saída: [1, 2, 3, 4, 5]

#Exercicio1: Dada a lista ['P', 'A', 'Y', 'A', 'T', 'H', 'O', 'N'], conte o numero de variáveos 'A' e utilize um loop para remover todos os 'A' excedente. 
lista_1 = ['P', 'A', 'Y', 'A', 'T', 'H', 'O', 'N']
# Contando o número de ocorrências de 'A'
contagem = lista_1.count('A')
print(f"O número de ocorrências de 'A' é: {contagem}")

# Removendo todos os 'A' excedentes
for _ in range(contagem):
    lista_1.remove('A')

print(f"Lista após remover os 'A' excedentes: {lista_1}")

#Exercicio2: Utilizando somente uma linha de programação, crie uma lista com os quadrados dos números de 1 a 51:
impares = [x**2 for x in range(1, 51)]
print(f"Lista com os quadrados dos números de 1 a 51: {impares}")

f_x = lambda x: x**2 + 1 
impares_lambda = list(map(f_x, range(1, 52)))
print(f"Lista com os quadrados dos números de 1 a 51 utilizando lambda: {impares_lambda}")

#Exercicio3: Criar um dicionário que correlacione as seguiintes listas:

valores = [1, 2, 3, 4, 5]
chaves = ['a', 'b', 'c', 'd', 'e']
dict_1 = {}

for i in range(5):
    dict_1[chaves[i]] = valores[i]
print(f"Dicionário correlacionando as listas: {dict_1}")

#Exercicio4: A partir do exercicio3, recriar as litas chaves e valores a partir do dicionário criado.
dict_3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
valores = list(dict_3.values())
chaves = list(dict_3.keys())
print(f"Lista de valores: {valores}")
print(f"Lista de chaves: {chaves}")
"""


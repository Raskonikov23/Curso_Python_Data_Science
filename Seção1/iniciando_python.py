"""
Listas servem para armazenar conjuntos de dados
lista_a = [1,2,3,4]
lista_b = ['abc', 3, 5, 6]

len(lista_a) # A len ver o tamanho que tem a lista declarada 

lista_1 = ['P', 'Y', 'T', 'H', 'O', 'N']
string1 = 'PYTHON'

print(lista_1[3]) # Vai imprimir a letra H
print(string1[:3]) # Vai imprimir a letra H
print(len(lista_1))
print(string1*2) # Vai imprmir o valor duas vezes. 

# Valores Booleanos

# == igual a 
# <= menor ou igual a
# >= maior ou igual a   
# !=  diferente de
# == atribuição de valor

#Condicionais if
numero = input('Digite um valor: ')
x = int(numero)
if x > 5:
    print('O valor é maior que 5')
elif x == 5:
    print('O valor é igual a 5')
else: 
    print('O valor é menor que 5')

if x > 5 and x < 10:
    print('O valor está entre 5 e 10')

elif x < 5 or x > 10:
    print('O valor é menor que 5 ou maior que 10')
    
else:
    print('O valor é igual a 5 ou igual a 10')

#Loop  for 

# É escrito para percorrer uma lista de valores, ou seja, ele vai percorrer cada elemento da lista e executar o que estiver dentro do bloco de código.
lista_valores = [1, 2, 3, 4, 5]
for valor in lista_valores:
    print(valor)
for valor in range(5):
    print(valor)

for valor in range(len(lista_valores)):
    print(lista_valores[valor])

for valor in enumerate(lista_valores):
    print(valor)
# Loop While
#Enquanto a condição for verdadeira, o loop while vai continuar executando o bloco de código.

x = 10 

while x > 0:
    print(x)
    x += 1
if x > 20:
    break
    
#Exercicio1, criar as condicionais para verificar se o número é positivo ou negativo, se for zero, retornar que é zero.

numero = input('Digite um valor: ')
if int(numero) >= 0:
    print('O valor é positivo') 
if int(numero) != 0:
    print('Não é um núemro')
elif int(numero) <= 0:
    print('O valor é negativo')

#Exercicio2, fazer um loop for para criar uma lista que intercale os valores da lisra a seguir:
#valores = [1, 2, 3, 4, 5]
#letras = ['a', 'b', 'c', 'd', 'e']
while True:
    valores = [1, 2, 3, 4, 5]
    letras = ['a', 'b', 'c', 'd', 'e']
    lista_intercalada = []
    for i in range(len(valores)):
        lista_intercalada.append(valores[i])
        lista_intercalada.append(letras[i])
    print(lista_intercalada)
    break
#Exercicio3. Dado um numero inteiro, fazer um operador while que calcule o fatorial desse número.
while True:
    numero = int(input('Digite um número inteiro: '))
    fatorial = 1
    contador = numero
    while contador > 1:
        fatorial *= contador
        contador -= 1
    print(f'O fatorial de {numero} é {fatorial}')
    break
#Desafio1: Criar uma lista com os 50 primeiros numeros primos. 

while True:
    primos = []
    numero = 1
    while len(primos) < 50:
        for i in range(2, numero):
            if numero % i == 0:
                break
        else:
            primos.append(numero)
        numero += 1
    print(primos)
    break
"""
#Desafio2: criar uma lista com as palavras formadas com a letra ARARA. 
#Utilizazndo a permutação de letras, criar uma lista com todas as palavras possíveis que podem ser formadas com a palavra ARARA.

lista_de_letras = ['A', 'R', 'A', 'R', 'A']
lista_de_palavras = []
iteracoes = 0

for i5 in range(len(lista_de_letras)):
    L5 = lista_de_letras[i5]
    Lista_L5 = lista_de_letras.copy()
    Lista_L4 = Lista_L5.copy()
    Lista_L4.pop(i5)

    for i4 in range(len(Lista_L4)):
        L4 = Lista_L4[i4]
        Lista_L3 = Lista_L4.copy()
        Lista_L3.pop(i4)

        for i3 in range(len(Lista_L3)):
            L3 = Lista_L3[i3]
            Lista_L2 = Lista_L3.copy()
            Lista_L2.pop(i3)

            for i2 in range(len(Lista_L2)):
                L2 = Lista_L2[i2]
                Lista_L1 = Lista_L2.copy()
                Lista_L1.pop(i2)

                for i1 in range(len(Lista_L1)):
                    L1 = Lista_L1[i1]
                    palavra = L5 + L4 + L3 + L2 + L1

                    if palavra not in lista_de_palavras:
                        lista_de_palavras.append(palavra)
                        iteracoes += 1

print(iteracoes)
print(lista_de_palavras)


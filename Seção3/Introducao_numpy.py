"""
#Numpy é uma biblioteca de computação científica para Python. Ela fornece suporte para 
# arrays multidimensionais e matrizes, além de uma coleção de funções matemáticas para operar 
# com esses arrays.

from time import time
import numpy as np
inicio = time()
lista_1 = list(range(10**6))
soma_1 = 0

for i in lista_1:
    soma_1 += i

fim = time()
print(f'Tempo de execução com listas: {fim - inicio:.6f} segundos')
print(f'Soma com listas: {soma_1}')

inicio = time()
array_1 = np.arange(10**8) #O método arange() do Numpy é usado para criar um array de números inteiros de 0 a 10^8 - 1.
soma_2 = np.sum(array_1)
fim = time()
print(f'Tempo de execução com Numpy: {fim - inicio:.6f} segundos ')
print(f'Soma com Numpy: {soma_2}')

#Operações com arrays (manipulando dados em arrays)

import numpy as np

cos = np.cos(np.pi) #Calcula o cosseno de pi, que é -1.0
print(cos)
sen  = np.sin(np.pi)
print(sen)

e = np.exp
print(e)

#Funções de criação de Arrays 
#Metodos para dimensionar uma array
# reshape, retorna um array com o shape indicado
# resize, modifica o shape da array em que está sendo aplicado 
import numpy as np

a_4 = np.ones(6)*11
print(a_4)

a_5 = np.eye(6)
print(a_5)

a_6 = np.arange(5)
print(len(a_6))

a_7 = np.linspace(0,10,12) #linspace serve para 
print(a_7.size)

a_8 = np.ones(8)
a_8.reshape
print(a_8)

a_9 = np.ones(8)
a_9.resize(2,4)
print(a_9)

a_10 = np.zeros(8)
a_10.resize
print(a_10)

a_11 = np.vstack((a_9, a_10))
print(a_11)

a_12 = np.hstack((a_9, a_10))
print(a_12)

#Metodo Copy()
# O metodo copy faz a copia (deep copy) do array. 

import numpy as np 

a = np.arange(8)
a[0]= 9
print(a)

b = a.copy()
print(b)

c = a.reshape(2,4)
print(c)

#Metodos Matematicos para Arrays 
# Max/Min retorna os valores de maximo e minimo
# Argmax/ argmin retorna os indices de valor max e min
# sum()/ mean()/ std() soma, média e desvio padrao 
# cumsum() retorna uma array com a soma acumulada 

import numpy as np

my_array = np.arange(8).reshape(2,4)**2
print(my_array.max(axis=1))
print(my_array.min())
print(my_array.sum())
print(my_array.cumsum())
"""

#Indices e Fatias de Arrays 

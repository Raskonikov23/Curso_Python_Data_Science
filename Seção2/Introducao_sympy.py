"""
#Sympy é uma biblioteca de álgebra computacional para Python. Ela fornece recursos para manipulação 
# simbólica de expressões matemáticas, incluindo simplificação, diferenciação, integração, resolução 
# de equações e muito mais.


x = sp.symbols('x')  # Define a variável simbólica x
print(x*x)  # Exibe a expressão simbólica x^2
print(sp.expand((x + 1)**2))  # Expande a expressão (x + 1)^2

#init_print() é uma função que inicializa o interpretador interativo do SymPy. Ela configura o ambiente 
#para que você possa trabalhar com expressões simbólicas de forma interativa, permitindo a entrada e 
# saída de expressões matemáticas.

import sympy as sp
sp.init_printing()  # Inicializa a impressão de expressões simbólicas

#lista_simbolos = ['y', 'z', 'w']  # Lista de nomes de símbolos
#x, y, z, w = sp.symbols(lista_simbolos)  # Cria símbolos y, z e w
#print(y + z + w)  # Exibe a expressão simbólica y + z + w

lista_simbolos = ['y', 'x']  # Lista de nomes de símbolos

x,y = sp.symbols(lista_simbolos)  # Cria símbolos y e z
print(y + x)  # Exibe a expressão simbólica y + z
print(sp.expand((y + x)**2))  # Expande a expressão (y + z)^2
print(sp.factor((y + x)**2))  # Fatora a expressão (y + z)^2
print(sp.simplify((y + x)**2))  # Simplifica a expressão (y + z)^2
print(sp.diff((y + x)**2, x))  # Diferencia a expressão (y + z)^2 em relação a x
"""
#Entendendo Matrizes e Vetores com Sympy
#Matrizes e vetores são estruturas matemáticas fundamentais que podem ser representadas e 
# manipuladas simbolicamente usando a biblioteca Sympy. A seguir, vamos explorar como criar e 
# operar com matrizes e vetores.

import sympy as sp

sp.init_printing()  # Inicializa a impressão de expressões simbólicas
"""
A = sp.Matrix([[1, 2], [3, 4]])  # Cria uma matriz 2x2
B = sp.Matrix([[5, 6, 7]])  # Cria uma matriz 2x3

print(A)             # Exibe a matriz A
print(A.det())       # Calcula o determinante
print(A.inv())       # Calcula a inversa
print(A.T)           # Calcula a transposta
print(A.eigenvals()) # Calcula os autovalores
print(A.eigenvects())# Calcula os autovetores
print(A.shape)       # Exibe as dimensões da matriz

print(B)             # Exibe a matriz B
print(B.shape)       # Exibe as dimensões da matriz B
"""
#Sistema linear de equações
#Um sistema linear de equações é um conjunto de equações lineares que podem ser representadas na 
# forma matricial Ax = b, onde A é a matriz dos coeficientes, x é o vetor das incógnitas e b é o 
# vetor dos termos constantes. O Sympy fornece ferramentas para resolver sistemas lineares de 
# equações simbolicamente.

x1, x2, x3 = sp.symbols(['x1', 'x2', 'x3'])  # Define as incógnitas do sistema
X = sp.Matrix([x1, x2, x3])  # Cria o vetor das incógnitas
E = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Cria a matriz dos coeficientes
R = sp.Matrix([10, 11, 12])  # Cria o vetor dos termos constantes

print(E*X - R)

#Parei na aula  Matrizes, pois não é meu foco aprender muita coisa desse módulo agora. 
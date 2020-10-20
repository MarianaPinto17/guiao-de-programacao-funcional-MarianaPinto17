#EXPRESSÕES LAMBDA
#Exercicio 4.1 - Dado um numero inteiro, retorna true caso o numero seja impar, False par
impar = lambda num: num%2==1 #true se resto é 1

#Exercicio 4.2
positivo = lambda num: num>0

#Exercicio 4.3 - Dados dois números, x e y, retorna True caso |x| < |y|, e False caso contrário
comparar_modulo = lambda x,y: abs(x) < abs(y)

#Exercicio 4.4 -  Dado um par (x, y), representando coordenadas cartesianas de um ponto no plano XY, retorna um par (r, θ), correspondente às coordenadas polares do mesmo ponto.
import math
cart2pol = lambda x,y: (math.sqrt(x*y + y*y), math.atan2(y,x))

#Exercicio 4.5 - Dadas três funções de duas entradas, f, g e h, retorna uma função de três entradas, x, y e z, cujo resultado é dado por: h(f (x, y), g(y, z))
ex5 = lambda f,g,h: lambda x,y,z: f(g(x,y), h(y,z))

#Exercicio 4.6 - quantificador universal - garante que todos os elementos obedecem à função passsada como argumento -> retorna true se todos obedecerem
def quantificador_universal(lista, f):
#    return [e for e in lista if f(e)]
    return [e for e in lista if not f(e)] == [] # mais eficiente

#Exercicio 4.7 - quantificador existencial - garante que pelo menos um elemento obedece à função passada como argumento -> retorna true se um obedecer
def quantificador_existencial(lista,f):
    return [1 for e in lista if not f(e)] == []

#Exercicio 4.9 - Dada uma lista com pelo menos um elemento e uma relação de ordem (ou seja, uma função
#booleana binária usada para comparação elemento a elemento), retorna o menor elemento
#da lista de acordo com essa relação de ordem.
def ordem(lista, f):
    if len(lista)==1:
        return lista[0]
    m = ordem(lista[1:], f) 
    
    return lista[0] if f(lista[0], m) else m

#Exercicio 4.10 - Dada uma lista com pelo menos um elemento e uma relação de ordem, retorna um par
#contendo o menor elemento da lista, de acordo com essa relação de ordem, e uma lista com
#os restantes elementos.
def filtrar_ordem(lista, f):
    if len(lista)==1:
        return [lista[0],[]]
    m, l = filtrar_ordem(lista[1:], f) # m é o menor, l é a cauda filtrada
    return (lista[0], lista[1:]) if f(lista[0], m) else (m, [lista[0]] + l)

#Exercicio 5.2 - Similar ao número anterior, mas sem restrição no tipo dos elementos da lista de entrada.
#A função de ordenação recebe, num parâmetro adicional, a relação de ordem (uma função
#binária booleana para comparação elemento a elemento) segundo a qual a lista de entrada
#deve ser ordenada
def ordenar_seleccao(lista, ordem):
    if len(lista) == 1:
        return lista
    m,l = filtrar_ordem(lista,ordem)

    return [m] + ordenar_seleccao(l,ordem)
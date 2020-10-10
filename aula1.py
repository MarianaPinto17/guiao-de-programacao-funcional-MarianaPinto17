#exercicio 1.1 - retorna o comprimento da lista
def comprimento(lista):
        if lista == []:
            return 0
        return 1 + comprimento(lista[1:])  #l[1:] apresenta todos os valores da lista tirando 
                                       #a primeira posição (a lista começa na posicao 0 e aqui começa na posicao 1)
                                       #, logo recursividade dá-nos o comprimento da lista 

#exercicio 1.2 - retorna a soma da lista de números
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:]) #l[0] dá return do primeiro valor da lista, logo primeiro valor mais todos os
                              # valores seguintes

#exercicio 1.3 - dada uma lista e um elemento, vê se o elemento ocorre na lista
def existe(lista, elem):
    if lista == []:
        return False
    if elem == lista[0]:
        return True
    return existe(lista[1:], elem)

#Exercicio 1.4 - concatenação de 2 listas
def concat(l1, l2):
	if l1 == []:
		return l2
	if l2 == []:
		return l1
	
	l1.append(l2[0]) # append acrescenta um elemento à lista

	return concat(l1, l2[1:])

#Exercicio 1.5 - retorna a lista inversa da dada
def inverte(lista):
	if lista == []:
		return []
	return inverte(lista[1:]) + [lista[0]]

#Exercicio 1.6 - capicua é ler o mesmo da esquerda direita e direita esquerda
def capicua(lista):
	#return lista = inverte(lista)
	if lista == []:
		return True
	return lista [0] == lista [-1] and capicua(lista[1:-1])
	
#Exercicio 1.7 - dada uma lista de listas, retorna a concatenação dessas listas
def explode(lista):
	if lista == []: # se a list estiver vazia retornamos lista vazia
		return []
	return concat(lista[0], explode(lista[1:]))

#Exercicio 1.8 - elemento x e elemento y, retorna outra lista em que x é substuido por y em todos os x
#original -> x; novo -> y;
def substitui(lista, original, novo):
	if lista == []:
		return []
	aux = lista[0]
	if aux == original:
		aux = novo
	return [aux] + substitui(lista[1:], original, novo)

#Exercicio 1.9 - Dadas duas listas ordenadas, calcular a união ordenadas mantendo repetições
def junta_ordenado(lista1, lista2):
	if lista1 == []:
		return lista2
	if lista2 == []:
		return lista1
	
	if lista1[0] < lista2[0]:
		return [lista1[0]] + junta_ordenado(lista1[1:], lista2) # vai a cabeça da lista numa lista + o resto da lista 1 mais a lista 2 toda

	return [lista2[0]] + junta_ordenado(lista1, lista2[1:])

#Exercício 1.10 - Dado um conjunto, em forma de lista, retorna uma lista de lista que representa o conjunto de todos os subconjuntos dados
def subconjuntos(lista):
	pass

#Exercicio 2.1 - dada uma lista de pares, produzir um par de listas dos 1os e 2os elementos
def separar(lista):
	if lista == []:
		return [], [] #tuplo é imutável, retornamos um tuplo com duas listas == ([],[])
	
	a,b = lista[0]

	l1, l2 = separar(lista[1:])
	
	return [a] + l1, [b] + l2

#Exercicio 2.2 - Dada uma lista l e um elemento x, retorna um par formado pela lista dos elementos de l
# diferentes de x e pelo número de ocorrências x em l.
def remove_e_conta(lista, elem):
	count = 0
	if lista == []:
		return []
	aux = lista[0]
	if aux == elem:
		lista.remove(elem)
		count = count + 1
	return remove_e_conta(lista[1:],elem)

#Exercicio 3.1 _ retorna a cabeça
def cabeca(lista):
	if lista == []:
		return lista
	
	return lista[0]

#Exercicio 3.2 - retorna a cauda
def cauda(lista):
	if lista == []:
		return lista

	return lista[-1]

#Exercicio 3.3 - Dado um par de listas com igual comprimento, produzir uma lista dos pares dos elementos homólogos.
def juntar(l1, l2):
    #zip -> juntar duas listas dois a dois os elementos numa lista, 
	# elemento a elemento criamos um par e colocar na cabeça da lista até as listas ficarem vazias
	if len(l1) != len(l2):		#verificação, se forem de tamanhos diferentes dá erro
		return None

	if l1 == []:				# paragem, se forem ambas vazias retorna lista vazia
		return []

	return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])

#Exercicio 3.4 - Dada uma lista de números, retorna o menor elemento.
def menor(lista):
	if lista == []:
		return None 		# se a lista for vazia não existe menor
	m = menor(lista[1:])
	
	if m and m<lista[0]:
		return m
	else:
		return lista[0]

#Exercicio 3.6
def max_min(lista):
	pass

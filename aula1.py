#exercicio 1.1
def comprimento(lista):
        if lista == []:
            return 0
        return 1 + comprimento(l[1:])  #l[1:] apresenta todos os valores da lista tirando 
                                       #a primeira posição (a lista começa na posicao 0 e aqui começa na posicao 1)
                                       #, logo recursividade dá-nos o comprimento da lista 

#exercicio 1.2
def soma(lista):
    if lista == []:
        return 0
    return l[0] + soma(l[1:]) #l[0] dá return do primeiro valor da lista, logo primeiro valor mais todos os
                              # valores seguintes

#exercicio 1.3
def existe(lista, elem):
    if lista = []
        return False
    if elem == l[0:]
        return True
    return False


#Exercicio 1.4
def concat(l1, l2):
	if l1 == []
		return l2
	if l2 == []
		return l1
	
	l1.append(l2[0]) # append acrescenta um elemento à lista

	return concat(l1, l2[1:])

#Exercicio 1.5
def inverte(lista):
	if lista == []
		return 0
	return inverte(lista[1:]) + (lista[0])

#Exercicio 1.6 - capicua é ler o mesmo da esquerda direita e direita esquerda
def capicua(lista):
	#return lista = inverte(lista)
	if lista == []
		return True
	#verificar
	return lista [0] = lista [-1] and capicua(lista[1:])
	
#Exercicio 1.7
def explode(lista):
	if lista == [] # se a list estiver vazia retornamos lista vazia
		return []
	return concat(lista[0], explode(lista[1:]))

#Exercicio 1.8
def substitui(lista, original, novo):
	if lista == []:
		return []

	if lista[0] == original
		return [novo] + substitui(lista[1:], original, novo)

#Exercicio 1.9
def junta_ordenado(lista1, lista2):
	if lista1 == []:
		return lista2
	if lista2 == []:
		return lista1
	
	if lista1[0] < lista2[0]
		return [lista1[0]] + junta_ordenado(lista1[1:], lista2) # vai a cabeça da lista numa lista + o resto da lista 1 mais a lista 2 toda

	return [lista2[0]] + junta_ordenado(lista1, lista2[1:])


#Exercicio 2.1
def separar(lista):
	if lista == []:
		return [], [] #tuplo é imutável, retornamos um tuplo com duas listas == ([],[])
	
	a,b = lista[0]

	l1, l2 = separar(lista[1:])
	
	return [a] + l1, [b] + l2

#Exercicio 2.2
def remove_e_conta(lista, elem):
	pass

#Exercicio 3.1
def cabeca(lista):
	pass

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
    #zip -> juntar duas listas dois a dois os elementos numa lista, 
	# elemento a elemento criamos um par e colocar na cabeça da lista até as listas ficarem vazias
	if len(l1) != len(l2)		#verificação, se forem de tamanhos diferentes dá erro
		return None

	if l1 == []:				# paragem, se forem ambas vazias retorna lista vazia
		return []

	return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])

#Exercicio 3.4
def menor(lista):
	if lista == []
		return None 		# se a lista for vazia não existe menor
	m = menor(lista[1:])

	if m and m<lista[0]:
			return m
		else:
			return lista[0]

#Exercicio 3.6
def max_min(lista):
	pass

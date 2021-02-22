#!/usr/bin/python3
#date: 21/02/2021

#Funcao que printa lista ou string ao contrario
#sem utilizar funcoes embutidas
#exemplo para List Comprehensions

teste = "hello"
x = ""
incrementador = 1

#INCREMENTADOR tem que ser 1 e nao 0.
#Pois se for 0, vai dar OUT OF RANGE, uma vez que listas em python
#começam com o indice 0, portanto seu tamanho, em indices, sempre sera
#len(lista)-1, e len(lista)-0 nao altera seu comprimento.

for item in range(len(teste)):
    if incrementador <= 5: # incrementador = 1
        #X = X + NUMERO DE INDICES DE TESTE - 1 (INCREMENTADOR)

        x = x + teste[len(teste)-incrementador] #teste[4], "o"
        incrementador = incrementador + 1 #incrementador = 2

print(x)

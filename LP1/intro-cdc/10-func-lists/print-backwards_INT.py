#!/usr/bin/python3
#date: 21/02/2021

#Funcao que printa lista ou string ao contrario
#sem utilizar funcoes embutidas

def backwards(n):
    saida = []
    for i in range(n):
        saida= saida + [n] #output.append(n)
        n = n - 1 #n -= 1
    return print(saida)

if __name__ == "__main__":
	backwards(int(input()))

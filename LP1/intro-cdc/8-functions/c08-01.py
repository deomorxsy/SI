#!/usr/bin/python3
#date: 14/02/2021
#Combinação Simples - Funções ex.1

def fatorial(x):
    fatorial = 1
    valor = x # Imutabilidade de variável
    for i in range(1, valor+1):
        if valor == 0:
            return 1
        if valor > 1:
            fatorial = fatorial * valor
            valor = valor - 1
    return fatorial

def main():
	m = int(input("Digite M: ")) #m elementos distintos
	n = int(input("Digite N: ")) #tomados n a n

	comb = fatorial(m)/(fatorial(n)*fatorial((m-n)))
	return print(comb)



if __name__ == "__main__":
	main()

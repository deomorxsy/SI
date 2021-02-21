#!/usr/bin/python3
#date: 08/02/2021

def main():
    n = int(input("Digite o valor de n: "))#10;
    aux1 = 0;
    acc = []
    aux2 = 0;

    print("\nDireita para a esquerda:")
    for i in range(1, n+1):
    	acc = acc + [i]
    	print("1/{}".format(i))
    	aux1 = aux1 + 1/i

    #print("\n")					#PRETTY PRINT
    print("=================") #PRETTY PRINT
    #print("\n")					#PRETTY PRINT
    
    print("Esquerda para a direita: ")
    for j in range(1, n+1):
    	print("1/{}".format(acc[-j]))
    	aux2 = aux2 + 1/acc[-j]
    print("\n")
    print("aux1 = {}".format(aux1))
    print("aux2 = {}".format(aux2))
    print("Booleano: {}".format(aux1==aux2))


if __name__ == '__main__':
    main()

#!/usr/bin/python3

#import math


#math.cos(x)

x = int(input("Digite X: ")) #cos que queremos descobrir
n = int(input("Digite N: ")) #numero de termos da serie
k = 1
aprox = 0

def fatorial(x):

    fatorial = 1
    valor = x #5

    for i in range(1, valor+1):
        if valor > 1:
            fatorial = fatorial * valor
            valor = valor - 1
    return fatorial


for i in range(1, n+1):
    aprox = aprox + ((+((-1)**i)) * (x**(2*i))/(2*fatorial(i)))
    print(aprox)
print(aprox)

#!/usr/bin/python3
#date: 14/02/2021

def main(k):
    ''' FATORIAL
    (int) -> int
    Recebe um inteiro k e retorna o valor de k!
    Pre-condição: supõe que k é um número inteiro não negativo.
    '''
    k_fat = 1

    aux = k
    acumulador = 0

    while k > 1:
        acumulador = k*(k-1)
        k = k - 1

    # COMPLETE ESSA FUNÇÃO

    return k_fat


if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main


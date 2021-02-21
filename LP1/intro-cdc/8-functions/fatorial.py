#!/usr/bin/python3
#date: 14/02/2021

def fatorial(n: int) -> int:
    n_fatorial = n  #Imutabilidade de k, var aux.
    contador = 1
    if n == 0:
        return 1
    while contador < n and n > 0:
        n_fatorial = n_fatorial * (n - contador)
        contador = contador + 1


    return n_fatorial

if __name__ == "__main__":
    print(fatorial(3))

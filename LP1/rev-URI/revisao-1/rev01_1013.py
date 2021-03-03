#!/usr/bin/python3
#date: 03/03/2021

def maiorab(a, b):
    #function that returns the large number in float
    return (a+b+abs(a-b))/2

def main():
    foobar = input()
    aux = 0
    bar = ["", "", ""]
    #como ja sabemos o numero de itens, podemos especificar strings


    #=========== QUEBRA-STRINGS ===========
    '''
    Tres laços fors para quebrar foobar, a string input,
    em tres partes, pulando espaços
    '''
    for i in range(len(foobar)):
        if foobar[i] == " ":
            aux = i + 1
            break
        bar[0] = bar[0] + foobar[i]
    #print(aux, bar)

    for i in range(aux, len(foobar)):
        if foobar[i] == " ":
            aux = i + 1
            break
        bar[1] = bar[1] + foobar[i]
    #print(aux, bar)

    for i in range(aux, len(foobar)):
        bar[2] = bar[2] + foobar[i]
    #print(aux, bar)

    #===========================================

    '''
    Como teremos que fazer várias conversões explícitas de int,
    podemos automatizar esse processo passando mais um laço for
    para transformar cada index de bar em int
    '''
    for i in range(len(bar)):
        bar[i] = int(bar[i])
    #print(type(bar[0]))

    '''
    Para comparar tres itens, o menor numero de usos da função maiorab é 2.
    Quer dizer que apenas duas comparações são necessárias para saber o maior
    número entre três entradas.
    '''
    foo = int(maiorab(int(bar[0]), int(bar[1])))
    return print("{} eh o maior".format( int(maiorab(foo, bar[2])) ))


if __name__ == "__main__":
    main()



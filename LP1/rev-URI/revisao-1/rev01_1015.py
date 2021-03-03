#!/usr/bin/python3
#date: 03/03/2021

def quebrachar(p):
    aux = 0
    pbar = ["", ""] #guardará dois valores. Os loops abaixo giram em torno disso.
    for i in range(len(p)):
        #varre a string em busca da ocorrencia.
        #Se o caractere for " ", atribua isso +1 à aux e pare.
        if p[i] == " ":
            aux = i + 1
            break
        pbar[0] = pbar[0] + p[i]
        #acima, é só ter cuidado com operacoes entre tipos de dados diferentes,
        #assim como o escopo i (da lista ou da variavel local) e do indice.
    for item in range(aux, len(p)):
        #especifica o inicio com aux e vai ate o final,
        #visto que agora nao tem mais espaços.
        pbar[1] = pbar[1] + p[item]

    for index in range(len(pbar)):
        #para todo indice dentro da lista pbar, transforme-o em float.
        pbar[index] = float(pbar[index])

    return pbar

def main():
    p1foo = input()
    p2foo = input()

    p1bar = quebrachar(p1foo)
    p2bar = quebrachar(p2foo)

    #formula da distancia entre dois pontos
    distance = ((p2bar[0]-p1bar[0])**2 + (p2bar[1]-p1bar[1])**2)**0.5
    return print("{:.4f}".format(distance))

if __name__ == "__main__":
    main()

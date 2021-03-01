#!/usr/bin/python3
#date: 01/03/2021

def filter(x): #line1
    tabela = {"code":"", "units":0, "price":""}
    aux = 0

    for i in range(len(x)):
        if x[i] != " ":
            aux = i
            tabela["code"] = tabela["code"] + x[i]
        else:
            aux = i
            break

    for item in range(aux, len(x)):
        if x[item] != " ":
            aux = item
            tabela["units"] += int(x[item])
            break
        #else:
            #aux = item
            #break

    for index in range(aux, len(x)):
        #print("aux = {}".format(aux)) #DEBUGGER
        if x[index] == " ":
            tabela["price"] += x[index+1:]
            break

    return tabela

def main():
    line1 = input()
    line2 = input()

    prod1 = filter(line1) #{"code":0, "units":0, "price":""}
    prod2 = filter(line2)

    #print("Units1:{}\nPrice1{}\n".format(type(prod1["units"]), type(prod1["price"])))
    total = (float(prod1["units"]) * float(prod1["price"])) + (float(prod2["units"]) * float(prod2["price"]))
    #print(total)
    return print("VALOR A PAGAR: R$ {:.2f}".format(total))



if __name__ == "__main__":
    main()



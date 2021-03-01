#!/usr/bin/python3

def main():

    salary = float(input())
    rombus = 0
    tax1, aux1 = 0, 0
    tax2, aux2 = 0, 0
    tax3, aux3 = 0, 0

    if salary <= 2000.00:
        return print("Isento")
    if salary > 2000.01 and salary <= 3000.00:
        aux1 = 1000 #salary - 2000.00
        tax1 = aux1 * 0.08
        return print(tax1)
    if salary > 3000.01 and salary <= 4500.00:
        aux2 = salary - 3000.01
        tax2 = aux2 * 0.18
        return print(tax2 + tax1)
    if salary > 4500.01:
        aux3 = salary - 4500.01
        tax3 = aux3 * 0.28
        return print(tax3 + tax2 + tax1)
if __name__ == "__main__":
    main()

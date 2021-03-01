#!/usr/bin/python3
#date: 03/01/2021

def main():
    seller_name = input() #seller's name
    fixed_sal = float(input()) #the seller fixed salary
    total = float(input()) #sale's total

    sal_total = fixed_sal + (total * 0.15)
    return print("TOTAL = R$ {:.2f}".format(sal_total))

if __name__ == "__main__":
    main()

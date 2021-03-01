#!/usr/bin/python3
#date: 01/03/2021

def main():
    e_number = int(input()) #employee's number
    whours = int(input()) #worked hours
    amount = float(input()) #amount received per hour

    return print("NUMBER = {}\nSALARY = U$ {:.2f}"
            .format(e_number, (whours * amount)))

if __name__ == "__main__":
    main()

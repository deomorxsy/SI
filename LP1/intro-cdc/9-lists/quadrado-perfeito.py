#!/usr/bin/python3

def main(number):
    #programa que printa NUMBER quantidade de
    #quadrados perfeitos

    squares = []

    for x in range(1, number):
        squares = squares + [x**2]

    return (print(squares))

if __name__ == "__main__":
    main(int(input()))

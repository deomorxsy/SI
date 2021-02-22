#!/usr/bin/python3

def main(number):
    #programa que printa NUMBER quantidade de
    #quadrados perfeitos
    squares = []
    squares = [item**2 for item in range(1, 10)]
    return print(squares)

if __name__ == "__main__":
    main(int(input()))




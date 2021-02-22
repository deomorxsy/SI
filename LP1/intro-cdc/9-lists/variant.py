#!/usr/bin/python3

def main(number):
    #programa que printa NUMBER quantidade de
    #quadrados perfeitos
    return print([item**2 for item in range(1, number)])


if __name__ == "__main__":
    main(int(input()))


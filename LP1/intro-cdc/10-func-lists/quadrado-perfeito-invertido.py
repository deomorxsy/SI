#!/usr/bin/python3

def main(number):
    squares = [x**2 for x in range(1, number)]
    for item in squares[::-1]:
        print(item)

if __name__ == "__main__":
    main(int(input()))

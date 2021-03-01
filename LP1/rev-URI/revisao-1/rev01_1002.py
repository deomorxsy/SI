#!/usr/bin/python3

def main():
    raio = float(input())
    pi = 3.14159

    area = pi * (raio**2)
    return print("A={:.4f}".format(area));

if __name__ == "__main__":
    main()

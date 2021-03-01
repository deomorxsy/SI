#!/usr/bin/python3
#date:01/03/2021

def main():
    raio = int(input())
    pi = 3.14159
    vol = ((4.0/3.0) * pi * (raio**3) )
    return print("VOLUME = {:.3f}".format(vol))

if __name__ == "__main__":
    main()

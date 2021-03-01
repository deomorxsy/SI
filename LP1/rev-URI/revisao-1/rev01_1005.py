#!/usr/bin/python3

def main(a, b):
    pa = 3.5   #peso a
    pb = 7.5   #peso b

    return (((pa * a) + (pb * b))/(pa + pb))

if __name__ == "__main__":
    print("MEDIA = {:.5f}".format(main(float(input()), float(input()))) )




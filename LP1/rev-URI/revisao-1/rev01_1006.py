#!/usr/bin/python3

def main(a, b, c):
    pa = 2   #peso a
    pb = 3   #peso b
    pc = 5

    return (((pa * a) + (pb * b) + (pc * c))/(pa + pb + pc))

if __name__ == "__main__":
    print("MEDIA = {:.1f}".format(
        main(float(input()),
            float(input()),
            float(input()))))




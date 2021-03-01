#!/usr/bin/python3

def main(n):

    if (n > 2 and n < 1000):
        for i in range(1,10+1):
            print("{} x {} = {}".format(i, n, (i*n) ))
            #return  (print("{} x {} = {}".format(i, n, (i*n) ))for i in range(1, 10+1))
if __name__ == "__main__":
    main(int(input()))

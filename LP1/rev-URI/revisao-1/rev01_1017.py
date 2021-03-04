#!/usr/bin/python3
#date: 03/03/2021

def main():
    hours = int(input())
    avgspeed = int(input())

    distance = hours * avgspeed

    return print("{:.3f}".format(distance/12))

if __name__ == "__main__":
    main()

#!/usr/bin/python3

def main():
    '''
    Returns a car's average consumption, the quotient of the
    total distance traveled (in Km) and the spent fuel total (in liters).
    '''
    foo = int(input()) #total distance in km
    bar = float(input()) # total spent fuel
    return print("{:.3f} km/l".format(foo/bar))

if __name__ == "__main__":
    main()

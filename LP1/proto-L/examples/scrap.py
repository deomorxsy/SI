#!/usr/bin/python3

import webbrowser, sys, requests

def main():
    if len(sys.argv) > 1:
        endereco = " ".join(sys.argv[1:])
    webbrowser.open("https://www.google.com/maps/place/" + endereco)

    res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
    print(type(res))
if __name__ == "__main__":
    main()

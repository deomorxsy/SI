#!/usr/bin/python3

import requests

def main():
    res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
    res.raise_for_status()

    arquivo = open("RomeuEJulieta.txt", "wb")

    for bloco in res.iter_content(100000):
        arquivo.write(bloco)
    arquivo.close()
if __name__ == "__main__":
    main()

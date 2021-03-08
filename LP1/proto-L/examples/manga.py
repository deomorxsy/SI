#!/usr/bin/python3

import requests, bs4, webbrowser
from datetime import date

dataAtual = date.today()
#dataTexto = dataAtual.strftime()i
dataTexto = "05/03/2021"

res = requests.get("http://centraldemangas.online/titulos/jujutsu-kaisen")
sopa = bs4.BeautifulSoup(res.text, "lxml")
update = sopa.select('small')

if dataTexto == update[0].getText():
    print("Tem novidade p/ hoje")
    link = sopa.select("tr td a")

    print("Abrindo capítulo...", link[0].getText())
    webbrowser.open(dominio + link[0].get('href'))

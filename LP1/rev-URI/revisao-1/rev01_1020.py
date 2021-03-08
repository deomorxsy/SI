#!/usr/bin/python3
#date: 07/03/2021

def ageDays(foo):
	anos = foo // 365
	fooAnos = foo % 365
	meses = fooAnos // 30
	dias = fooAnos % 30
	return print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos, meses, dias))

if __name__ == "__main__":
	ageDays(int(input()))

#!/usr/bin/python3
#date: 03/03/2021

def main():
	notes = int(input())
	foo = notes #Imutabilidade
	bar = []
	troco = [100, 50, 20, 10, 5, 2, 1]

	print(foo)
	for i in range(len(troco)):
		if foo // troco[i] > 0:
			bar = bar + [foo // troco[i]]
			foo = foo % troco[i]
		else:
			bar = bar + [0]
		print("{} nota(s) de R$ {},00".format(bar[i], troco[i]))

if __name__ == "__main__":
	main()


#!/usr/bin/python3
#date:03/03/2021

def main():

	foobar = input();
	a_foo = "";
	b_ar = "";
	c_hoge = "";
	pi = 3.14159;

	for i in range(len(foobar)):
		if foobar[i] == " ":
			aux = i+1; #atribue o indice +1 a variavel, pulando ele
			break;
		a_foo = a_foo + foobar[i]

	for item in range(aux, len(foobar)):
		if foobar[item] == " ":
			aux = item+1; #pula esse indice e atribui o proximo a aux
			break;
		b_ar = b_ar + foobar[item];

	for index in range(aux, len(foobar)):
		c_hoge = c_hoge + foobar[index];

	'''debug
	print(a_foo)
	print(b_ar)
	print(c_hoge)
	'''
	a_foo = float(a_foo)
	b_ar = float(b_ar)
	c_hoge = float(c_hoge)

	triangulo = (a_foo*c_hoge)/2;
	circulo = pi*(c_hoge**2);
	trapezio = ((a_foo + b_ar)*c_hoge)/2;
	quadrado = (b_ar**2);
	retangulo = (a_foo * b_ar);

	return print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(triangulo, circulo, trapezio, quadrado, retangulo))

if __name__ == "__main__":
	main()

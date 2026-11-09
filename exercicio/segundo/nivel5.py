#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero_digitado = int(input('digite o numero: '))

for i in range(0,10,1):
    print(numero_digitado, 'x', i, '=', numero_digitado * i)
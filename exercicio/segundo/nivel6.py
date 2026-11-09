#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_numeros = [10, 5, 8, 3, 7] #crie uma lista
soma = 0

try:
    for numero in lista_numeros: #utilize o loop
        soma += numero #calculo da soma
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#try: o Python tenta executar o que está dentro.
#except: se algo der erro lá dentro, ele pula para cá, em vez de mostrar aquele erro vermelho.
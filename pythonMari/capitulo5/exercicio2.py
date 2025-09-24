def resultadoFinal(numeroSomados, valor):
    print(f"Somando todos os valores e subtraindo por 10 o resultado é {numeroSomados - valor}")


numero = int(input('Informe um número inteiro: '))
numero1 = int(input('Informe outro número inteiro: '))
numero2 = int(input('Informe mais um número inteiro: '))
numero3 = int(input('Informe o último número inteiro: '))
numeroSomados = (numero + numero1 + numero2 + numero3)
valor = 10

resultadoFinal(numeroSomados, valor)
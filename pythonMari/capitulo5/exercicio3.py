def resultadoSoma(numero, numero1):
    print(f'Resultado da soma dos números é: {numero + numero1}')


def resultadoSubtracao(numero, numero1):
    print(f'Resultado da subtração dos números é: {numero - numero1}')


def resultadoMultiplicacao(numero, numero1):
    print(f'Resultado da multiplicação dos números é: {numero * numero1}')


def resultadoDivisao(numero, numero1):
    print(f'Resultado da divisão dos números é: {numero / numero1}')


numero = int(input("Digite um número inteiro: "))
numero1 = int(input("Digite outro número inteiro: "))

resultadoSoma(numero, numero1)
resultadoSubtracao(numero, numero1)
resultadoMultiplicacao(numero, numero1)
resultadoDivisao(numero, numero1)
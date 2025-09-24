def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1,  numero2):
    return numero1 - numero2

def multiplicacao(numero1,  numero2):
    return numero1 * numero2

def divisao(numero1,  numero2):
    return numero1 / numero2


numero1 = int(input("Digite um número inteiro "))
numero2 = int(input("Digit um numero inteiro "))

resultadosoma = soma(numero1, numero2)
resultadosubtracao =subtracao(numero1, numero2)
resultadomultiplicacao = multiplicacao(numero1, numero2)
resultadodivisao = divisao(numero1, numero2)

print("O resultado da função soma", resultadosoma)
print("O resultado da função subtracao", resultadosubtracao)
print("O resultado da função multiplicacao", resultadomultiplicacao)
print("O resultado da função divisao", resultadodivisao)


def resultadoTabuada(numero, tabuada):
    while tabuada <= 10:
        print(f' {numero} x {tabuada} = {numero * tabuada}')
        tabuada += 1

numero = int(input("Insira um número inteiro: "))
tabuada = 1
resultadoTabuada(numero, tabuada)
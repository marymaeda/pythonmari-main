precocapalivro = 24.95
precocapalivroDesconto = precocapalivro - (precocapalivro * 0.40)
custoFretePrimeiroExemlar =  precocapalivroDesconto + 3.00
custoFreteRestanteExemlar = precocapalivroDesconto + 0.75
custototalAtacado = custoFretePrimeiroExemlar + (custoFreteRestanteExemlar * 59)

print("O preco total de atacado para 60 exemplares é de:", custototalAtacado)
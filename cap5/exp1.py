def validalogin(nome, senha):
    if (nome == "Mariana" and senha == "senha123"):
        return print("seja bem vindo", nome, senha)
    else:
        return print("senha ou login inválidos")

print("=== Digite seu nome ====")
nome = input()
print("=== Digite sua senha ===")
senha = input()

validalogin(nome, senha)
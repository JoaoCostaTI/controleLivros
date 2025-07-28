try:
    # Código que pode gerar um erro
    numero = int(input("Digite um número: "))
    print(f"Você digitou {numero}")
except:
    # Código executado se ocorrer qualquer erro
    print("Ocorreu um erro!")
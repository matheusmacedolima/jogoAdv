palavras = ["python", "computador", "mouse", "teclado", "internet"]

for palavra in palavras:
    print("\nDica: é uma palavra relacionada à tecnologia")

    tentativa = ""

    while tentativa != palavra and tentativa != "desistir":
        tentativa = input("Digite sua tentativa: ")

    if tentativa == palavra:
        print("Acertou!")
    else:
        print(f"Você desistiu. A palavra era {palavra}")
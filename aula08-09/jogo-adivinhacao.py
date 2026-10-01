def descobrir(letra, palavra, lista):
    for i in palavra:
        if letra == i:
            print("tem essa letra")
            return True
    else:
        if letra in lista:
            print("essa letra ja esta preenchida")
            return False
        print("nao tem essa letra")
        return False


def adicionar(lista, letra):
    if letra not in lista:
        lista.append(letra)


def mostrar(lista, original):
    for letra in original:
        for i in lista:
            if i == letra:
                print(i, end=" ")
                break
        else:
            print("_", end=" ")
    print()


original = "banana"
palavra = set(original)
lista = []
i = 0
p = ""

while True:
    if i == 6:
        print("perdeu")
        break

    letra = input("Digite uma letra: ")
    resultado = descobrir(letra, palavra, lista)

    if resultado:
        adicionar(lista, letra)
        palavra.remove(letra)
        p += letra

    else:
        i += 1

    mostrar(lista, original)

    if len(palavra) == 0:
        print("venceu")
        break

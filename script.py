import os

def calculo_media(numeros):
    return sum(numeros) / len(numeros)

def calculo_desvios(numeros, media):
    return [(numero - media) ** 2 for numero in numeros]

def variancia_desvio(desvios):
    return round(sum(desvios) ** (1/2), 5)

def input_dado():
    while True:
        try:
            return float(input("Digite um número: "))
        except ValueError:
            print("\n--> Apenas números são permitidos <--\n")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("1. Adicionar número")
    print("2. Calcular média e desvio padrão")
    print("3. Reiniciar e começar do zero")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    numeros = []

    while True:
        limpar_tela()
        opcao = mostrar_menu()

        if opcao == '1':
            numeros.append(input_dado())
        elif opcao == '2':
            if numeros:
                media = calculo_media(numeros)
                desvios = calculo_desvios(numeros, media)
                print("\nNúmeros:", numeros)
                print("Média: {:.5f}".format(media))
                print("Desvio padrão: {:.5f}".format(variancia_desvio(desvios)))
            else:
                print("\nNenhuma número foi adicionado.")
        elif opcao == '3':
            numeros.clear()
        elif opcao == '4':
            break
        else:
            print("\nOpção inválida!")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()

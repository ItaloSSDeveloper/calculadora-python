def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def menu():
    while True:
        print("\n=== Calculadora Python ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando...")
            break

        if opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except:
                print("Entrada inválida")
                continue

            if opcao == "1":
                print("Resultado:", somar(num1, num2))
            elif opcao == "2":
                print("Resultado:", subtrair(num1, num2))
            elif opcao == "3":
                print("Resultado:", multiplicar(num1, num2))
            elif opcao == "4":
                print("Resultado:", dividir(num1, num2))
        else:
            print("Opção inválida")


if __name__ == "__main__":
    menu()
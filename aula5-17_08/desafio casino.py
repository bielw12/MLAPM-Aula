import random
import time
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def animacao_carregamento(texto):
    print(texto, end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()


def jogar_caca_niqueis(saldo):
    print("\n" + "=" * 40)
    print("       🎰 MÁQUINA CAÇA-NÍQUEIS 🎰")
    print("=" * 40)

    try:
        aposta = int(input(f"Seu saldo atual: R$ {saldo}\nDigite o valor da sua aposta: R$ "))
    except ValueError:
        print("Valor inválido!")
        return saldo

    if aposta <= 0 or aposta > saldo:
        print("❌ Aposta inválida! Verifique seu saldo.")
        return saldo

    simbolos = ["🍒", "🍋", "🔔", "⭐", "💎", "7️⃣"]

    animacao_carregamento("Girando os rolos")

    # Sorteia 3 símbolos
    resultado = [random.choice(simbolos) for _ in range(3)]

    print("\n+-----+-----+-----+")
    print(f"|  {resultado[0]}  |  {resultado[1]}  |  {resultado[2]}  |")
    print("+-----+-----+-----+")

    # Verifica premiação
    if resultado[0] == resultado[1] == resultado[2]:
        premio = aposta * 10
        print(f"\n🎉 JACKPOT! Três {resultado[0]} iguais! Você ganhou R$ {premio}!")
        saldo += premio
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        premio = aposta * 2
        print(f"\n✨ Boa! Dois símbolos iguais. Você ganhou R$ {premio}!")
        saldo += premio
    else:
        print(f"\n😢 Não foi dessa vez. Você perdeu R$ {aposta}.")
        saldo -= aposta

    return saldo


def jogar_roleta(saldo):
    print("\n" + "=" * 40)
    print("         🎯 ROLETA DA SORTE (0 a 10) 🎯")
    print("=" * 40)

    try:
        aposta = int(input(f"Seu saldo atual: R$ {saldo}\nDigite o valor da sua aposta: R$ "))
    except ValueError:
        print("Valor inválido!")
        return saldo

    if aposta <= 0 or aposta > saldo:
        print("❌ Aposta inválida!")
        return saldo

    try:
        escolha = int(input("Escolha um número entre 0 e 10: "))
    except ValueError:
        print("Número inválido!")
        return saldo

    if escolha < 0 or escolha > 10:
        print("❌ Escolha um número entre 0 e 10!")
        return saldo

    animacao_carregamento("A roleta está girando")

    sorteado = random.randint(0, 10)
    print(
    número
    sorteado
    foi: {sorteado})

    if escolha == sorteado:
        premio = aposta * 8
        print(f"\n🎯 Na mosca! Você acertou e ganhou R$ {premio}!")
        saldo += premio
    else:
        print(f"\n❌ Errou! Você perdeu R$ {aposta}.")
        saldo -= aposta

    return saldo


def main():
    saldo = 100  # Saldo inicial

    while saldo > 0:
        limpar_tela()
        print("=" * 40)
        print("        💰 BEM-VINDO AO PYTHON CASSINO 💰")
        print("=" * 40)
        print(f"💳 Saldo Disponível: R$ {saldo}")
        print("\nEscolha o jogo:")
        print("1. Caça-Níqueis (Slots)")
        print("2. Roleta de Números")
        print("3. Sair do Cassino")

        opcao = input("\nDigite sua opção (1-3): ")

        if opcao == '1':
            saldo = jogar_caca_niqueis(saldo)
        elif opcao == '2':
            saldo = jogar_roleta(saldo)
        elif opcao == '3':
            print("\nObrigado por jogar! Volte sempre que quiser arriscar a sorte.")
            break
        else:
            print("❌ Opção inválida!")

        input("\nPressione [Enter] para continuar...")

    if saldo <= 0:
        limpar_tela()
        print("=" * 40)
        print("          💸 GAME OVER 💸")
        print("Você faliu! Suas fichas acabaram.")
        print("=" * 40)


if __name__ == "__main__":
    main()
import random

def jogar():
    while True:
        # Solicita ao jogador que escolha pedra, papel ou tesoura
        jogador_escolha = input("Escolha pedra, papel ou tesoura: ").lower()
        
        # Verifica se a escolha do jogador é válida
        if jogador_escolha not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Tente novamente.")
            continue
        
        # Gera uma escolha aleatória para o computador
        opcoes = ["pedra", "papel", "tesoura"]
        computador_escolha = random.choice(opcoes)
        
        # Exibe as escolhas do jogador e do computador
        print(f"Você escolheu {jogador_escolha}.")
        print(f"O computador escolheu {computador_escolha}.")
        
        # Determina o resultado do jogo
        if jogador_escolha == computador_escolha:
            print("Empate!")
        elif (
            (jogador_escolha == "pedra" and computador_escolha == "tesoura") or
            (jogador_escolha == "papel" and computador_escolha == "pedra") or
            (jogador_escolha == "tesoura" and computador_escolha == "papel")
        ):
            print("Você venceu!")
        else:
            print("O computador venceu!")
        
        # Pergunta ao jogador se deseja jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != "s":
            break

if __name__ == "__main__":
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    jogar()

    # Jogo pedra, papel e tesoura . PEGUEI A RESPOSTA PRA ESTUDAR O CODIGO !!!!
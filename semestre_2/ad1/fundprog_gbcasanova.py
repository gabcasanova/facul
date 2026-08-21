#========================================#
#= NOME: Gabriel Babo Casanova          =#
#= CURSO: Computação-CEDERJ-UFF         =#
#= POLO: Rocinha                        =#
#= CPF: 145.200.397-11                  =#
#= MATRÍCULA: 26113050056               =#
#= MATÉRIA: Fundamentos de Programação  =#
#= DATA: 21 de Agosto de 2026           =#
#========================================#

# Importar Bibliotecas
import random
#-------------------------------------------------

def sortear_palavra():
    banco_palavras = [
        'CACHORRO', 'GATO', 'CELULAR', 'COMPUTADOR', 'FACULDADE', 'VITROLA',
        'MICROFONE', 'TELEVISÃO', 'MESA', 'CADEIRA', 'CANETA', 'ESCOLA', 'CADERNO',
        'VIDEOGAME', 'LIVRO', 'ESTANTE', 'INSTANTE', 'TESOURA', 'DESENHO',
        'CALCULADORA', 'MÁQUINA', 'SABÃO', 'CHUVEIRO', 'VASO', 'REFRIGERANTE', 'CHOCOLATE',
        'AÇÚCAR'
    ]
    palavra_sorteada = random.choice(banco_palavras)
    return palavra_sorteada

# Definições gerais
jogo_rodando = True
estado_jogo = "menu"

numero_partidas = 0
numero_vitorias = 0
numero_derrotas = 0

# Definições de partida
vida = 6
mensagem_atual = ""
palavra_real = sortear_palavra()
letras_descobertas = []
letras_escolhidas = []

def menu_principal(numero_partidas, numero_vitorias, numero_derrotas, mensagem):
    estado_jogo = "menu"
    jogo_rodando = True

    # Calcular aproveitamento do jogador, como não pode dividir por zero,
    # se o numero de partidas for zero, substituir por string
    if numero_partidas > 0:
        percentual_aproveitamento = str(int((numero_vitorias / numero_partidas) * 100)) + "%" # transformar em inteiro pra evitar dizima
    else:
        percentual_aproveitamento = "0%"

    print("-------------------- JOGO da FORCA ------------------------")
    print("")
    print(mensagem)
    print("")
    print("Número de partidas jogadas:", numero_partidas)
    print("Número de vitórias:", numero_vitorias)
    print("Número de derrotas:", numero_derrotas)
    print("Percentual de aproveitamento: ", percentual_aproveitamento)
    print("")
    print("Opções:")
    print("[ 1 - Iniciar uma Nova Partida ]")
    print("[ 2 - Sair do Jogo             ]")
    print("")
    print("-----------------------------------------------------------")
    print("")
    escolha = str(input("Escolha uma opção: "))
    print("")

    # Condição de escolhas do menu
    if escolha == "1":
        estado_jogo = "forca"
        mensagem=""
    elif escolha == "2":
        jogo_rodando = False
    else:
        mensagem = "Escolha uma opção existente!"
        estado_jogo = "menu"

    return estado_jogo, jogo_rodando,mensagem

def desenhar_letreiro(palavra_real, letras_descobertas):
    letreiro = ""
    # Para cada letra na palavra...
    for letra in palavra_real:
        # Se a letra da palavra já foi adivinhada pelo usuário...
        if letra in letras_descobertas:
            letreiro += letra + " "  # Mostra a letra
        else:
            letreiro += "_ "  # Mostra o traço pras letras não descobertas ainda

    print("Palavra: [ " + str(letreiro) + "]")

def checar_letra(vida, palavra_real, letras_descobertas, letras_escolhidas):
    alfabeto_completo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Formatar a letra escolhida pelo usuário para maiúscula para manter consistência
    tentativa = str(input("Digite uma letra: ")).upper()

    vidas_temp = vida
    mensagem_atual = ""
    estado_jogo = "forca"

    # Permitir somente uma letra
    if len(tentativa) == 1:
        # Checar se a letra já não foi escolhida
        if tentativa not in letras_escolhidas:
            # Checar por acentos e caractres especiais pra ficar mais facil pro jogador
            variacoes = [tentativa]

            if tentativa == 'A':
                variacoes = ['A', 'Á', 'Ã', 'Â', 'À']
            elif tentativa == 'E':
                variacoes = ['E', 'É', 'Ê']
            elif tentativa == 'I':
                variacoes = ['I', 'Í']
            elif tentativa == 'O':
                variacoes = ['O', 'Ó', 'Õ', 'Ô']
            elif tentativa == 'U':
                variacoes = ['U', 'Ú']
            elif tentativa == 'C':
                variacoes = ['C', 'Ç']

            # Ver se o jogador acertou pelo menos uma das variações
            acertou_alguma = False

            for variacao in variacoes:
                if variacao in palavra_real:
                    acertou_alguma = True

                    if variacao not in letras_descobertas:
                        letras_descobertas.append(variacao)

            # Checar o resultado final
            if acertou_alguma == False:
                vidas_temp -= 1
                mensagem_atual = "A palavra não possui essa letra."

            # Adicionar ao banco de letras escolhidas
            letras_escolhidas.append(tentativa)
        else:
            mensagem_atual = "Essa letra já escolhida!"
    else:
        mensagem_atual = "Digite apenas uma letra!"

    # Checar se cada letra na palavra já foi descoberta, se sim,
    # vencer o jogo.
    acertou_tudo = True

    for letra in palavra_real:
        if letra not in letras_descobertas:
            acertou_tudo = False

    if acertou_tudo == True:
        estado_jogo = "vitoria"

    return vidas_temp, mensagem_atual, estado_jogo

def desenhar_personagem(vida):
    # String de varias linhas com os gráficos do desenho da forca
    telas_personagem = [
"""
 +---+,
 |   |
 O   |,
/|\\  |,
/ \\  |,
     |,
 =========
""",

"""
 +---+,
 |   |
 O   |,
/|\\  |,
/     |,
     |,
 =========
""",

"""
 +---+,
 |   |
 O   |,
/|\\  |,
     |,
     |,
 =========
""",

"""
 +---+,
 |   |
 O   |,
/|   |,
     |,
     |,
 =========
""",

"""
+---+,
|   |
O   |,
|   |,
    |,
    |,
=========
""",

"""
+---+,
|   |
O   |,
    |,
    |,
    |,
=========
""",

"""
+---+,
|   |
    |,
    |,
    |,
    |,
=========
""",
    ]
    print(telas_personagem[vida])

# Loop do jogo
while jogo_rodando == True:
    if estado_jogo == "menu":
        # Resetar variáveis
        vida = 6
        palavra_real = sortear_palavra()
        letras_descobertas = []
        letras_escolhidas = []

        # Menu principal
        estado_jogo, jogo_rodando, mensagem_atual = menu_principal(numero_partidas, numero_vitorias, numero_derrotas, mensagem_atual)

    elif estado_jogo == "forca":
        if vida > 0:
            # Perguntas ao jogador enquanto ainda possui vida
            print("-------------------- JOGO da FORCA ------------------------")

            # Desenhar personagem
            desenhar_personagem(vida)

            # Desenhar letreiro
            desenhar_letreiro(palavra_real, letras_descobertas)
            print("Letras Escolhidas:", letras_escolhidas)
            print("Tentativas restantes:", vida)

            print("")
            print("-----------------------------------------------------------")
            print("")

            # Checar letra no teclado
            print(mensagem_atual)
            vida, mensagem_atual, estado_jogo = checar_letra(
                vida,
                palavra_real,
                letras_descobertas,
                letras_escolhidas
            )
            print("")
        else:
            estado_jogo = "derrota"

    elif estado_jogo == "derrota":
        print("-------------------- JOGO da FORCA ------------------------")
        desenhar_personagem(0)
        print("Você perdeu! A palavra correta era: ")
        print(palavra_real)
        print("")
        print("")
        print("-----------------------------------------------------------")
        print("")
        input("Pressione qualquer tecla para continuar... ")
        print("")

        # Estado de derrota, retornar ao menu
        numero_derrotas += 1
        numero_partidas += 1
        mensagem_atual = "Que pena! Você perdeu."
        estado_jogo = "menu"

    elif estado_jogo == "vitoria":
        print("-------------------- JOGO da FORCA ------------------------")
        desenhar_personagem(vida)
        print("Você acertou! A palavra correta era: ")
        print(palavra_real)
        print("")
        print("")
        print("-----------------------------------------------------------")
        print("")
        input("Pressione qualquer tecla para continuar... ")
        print("")

        # Estado de vitória, retornar ao menu
        numero_vitorias += 1
        numero_partidas += 1
        mensagem_atual = "Parabéns! Você acertou."
        estado_jogo = "menu"

import random

def jogar_forca():

    imprime_msg_abertura()

    #arquivo = open('palavras.txt', 'w')
    #arquivo.write('banana\n')
    #arquivo.write('melancia\n')       ## CRIA O ARQUIVO PELO PYTHON
    #arquivo.write('morango\n')
    #arquivo.write('maça')
    #arquivo.close()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ['_' for letra in palavra_secreta] #teve que colocar palavra_secreta para a função receber e retornar
                                                        # pois quando cria a função, as variaveis só existem dentro delas
    #for letra in palavra:
     #   letras_acertadas.append('_')

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta) #Como as variaveis nao sao criadas nessa função
        else:                                                             # colocar elas entre "()" e não no "return"
            erros += 1
            desenha_forca(erros)

        enforcou = (erros == 7)
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)


    if (enforcou):
        imprime_mensagem_perdedor(palavra_secreta)
    else:
        imprime_mensagem_vencedor()


def imprime_msg_abertura():
    print('*' * 33)
    print('Bem vindo ao jogo da Forca!')
    print('*' * 33)

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')  # Lê o arquivo
    palavras = []
    for linha in arquivo:
        linha = linha.strip()  # tira os \n e espaços
        palavras.append(linha)
    arquivo.close()

    num = random.randrange(0, len(palavras))
    palavra_secreta = palavras[num].upper()  # escolher uma palavra do arquivo aleatoriamente
    return palavra_secreta

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1  # Posição está ligada de forma indireta às posições das letras nas palavras
        # Se roda a condição e não é verdadeira, posicao soma +1 e vai acompanhando a "letra"
        # com o +1 no final da condição.


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == '__main__'): #Verifica se está chamando "forca.py" diretamente ou pelo arquivo "jogo" e roda se
    jogar_forca()            # estiver chamando diretamente pelo forca.py
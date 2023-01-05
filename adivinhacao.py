from random import randint

def jogar_adivinhacao():
    print('*' * 33)
    print('Bem vindo ao jogo de adivinhação!')
    print('*' * 33)

    numero_secreto = randint(1, 100)
    tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?', end="\n")
    print('[1] - Fácil \n[2] - Médio \n[3] - Díficil')

    nivel = int(input('Digite o nível: '))

    if (nivel == 1):
        tentativas = 10
    elif (nivel == 2):
        tentativas = 5
    elif (nivel == 3):
        tentativas = 3
    else:
        print('\nNúmero inválido!')



    for rodada in range(1, tentativas + 1):
        print('Tentativa {} de {}' .format(rodada, tentativas))
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou', chute)

        if (chute < 1) or (chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue #continuar com o laço

        if (numero_secreto == chute):
            print(f'Você acertou e fez {pontos}!')
            break  #sair do laço
        else:
            if(chute > numero_secreto):
                print('Você errou! O seu chute foi maior do que o número secreto.')
                if (rodada == tentativas):
                    print('\nVocê fez {} pontos.' .format(pontos))
            else:
                print('Você errou! O seu chute foi menor do que o número secreto.')
                if (rodada == tentativas):
                    print('\nVocê fez {} pontos.' .format(pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    if (nivel == 1) or (nivel == 2) or (nivel == 3):
        print(f'\nO número secreto era {numero_secreto}')
        print('Fim do Jogo!')
    else:
        print('Reinicie e insira um nível válido!')

if (__name__ == '__main__'):  #Verifica se está chamando "adivinhacao.py" diretamente ou pelo arquivo "jogo" e roda se
    jogar_adivinhacao()       # estiver chamando diretamente pelo adivinhacao.py
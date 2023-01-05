import forca
import adivinhacao

print('*' * 33)
print('Escolha o seu jogo!')
print('*' * 33)

print('(1) Forca \n(2) Adivinhação')

jogo = int(input('Qual jogo deseja jogar? '))

if(jogo == 1):
    print('Jogando Forca')
    forca.jogar_forca()
elif(jogo == 2):
    print('Jogando Adivinhação')
    adivinhacao.jogar_adivinhacao()
else:
    print('Opção inválida!')
    print('Fim.')


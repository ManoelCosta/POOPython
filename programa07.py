print('****************************')
print('*** JOGO DE ADIVINHAÇÕES ***')
print('****************************')
print('')
nivel = int(input('Nivel 1\nNivel 2\nNivel 3\nEscolha o nivel:\n'))

numero_secreto = 42
total_de_tentativas = 0
pontuacao = 1000
if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5
else:
    print('Valor incorreto')


for rodada in range(1, total_de_tentativas+1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    print('Pontuação: {}'.format(pontuacao))

    chute = int(input('Tente adivinhar o numero:\n'))
    print('Você digitou', chute)

    pontuacao = abs(pontuacao - (chute - numero_secreto))

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou')
        break
    elif maior:
        print('Errou! Digitou um numero maior')
    elif menor:
        print('Errou! Digitou um numero menor')
print('Fim de jogo!')
print('Placar final: {} pontos'.format(pontuacao))

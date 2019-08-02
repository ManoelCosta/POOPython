print('***************************')
print('*** JOGO DA ADIVINHAÇÃO ***')
print("***************************")

numero_secreto = 19
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Tente adivinhar o numero:\n'))
    print('Você chutou o numero {}'.format(chute))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Parabéns! Você acertou')
        print('Você digitou {} e eu estava pensando em {}'.format(chute, numero_secreto))
        break
    elif maior:
        print('Que pena, você errou, chutou um numero maior')
    elif menor:
        print('Que pena, você errou, chutou um numero menor')
    rodada = rodada + 1
print('Fim de jogo')

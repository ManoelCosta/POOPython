print('*+'*14)
print('*+   JOGO DA ADIVINHAÇÃO  *+')
print('*+'*14)
numero_secreto = 32
chute = int(input('Tente adivinhar o numero:\n'))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if acertou:
    print('Parabéns você acertou')
elif maior:
    print('Que pena, você errou, chutou um numero maior')
elif menor:
    print('Que pena, você errou, chutou um numero menor')
print('Fim de jogo')

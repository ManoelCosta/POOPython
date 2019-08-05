#Utilizando o laço de repetição while

print('***************************')
print('*** Jogo da Adivinhação ***')
print('***************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    
    chute = int(input('Tente adivinhar o número:\n'))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você Ganhou!')
        break
    elif (maior):
        print('você chutou um número maior')
    elif (menor):
        print('você chutou um número menor')

    rodada += 1

print('Fim de jogo')

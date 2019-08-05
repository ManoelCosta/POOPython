#Utilizando o laço de repetição for
print('***************************')
print('*** Jogo da Adivinhação ***')
print('***************************')

numero_secreto = 42
pontuacao = 1000
nivel = int(input('Escolha o Nivel:\nNivel 1 = 20 Tentativas\nNivel 2 = 10 tentativas\nNivel 3 = 5 Tentativas\n'))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
elif (nivel == 3):
    total_de_tentativas = 5
else:
    print('Digitou um valor incorreto')
    exit()
    print('Fim de Jogo')
for rodada in range(1, total_de_tentativas + 1):
    print('Pontuação: ', pontuacao)
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

    pontuacao = abs(pontuacao - (chute - numero_secreto))

print('Pontuação Final: ', pontuacao)
print('Fim de jogo')

print('*'*21)
print('*** JOGO DA FORCA ***')
print('*'*21)

palavra_secreta = 'flamengo'
letras_acertadas = ['_', '_', '_', '_', '_', '_', '_', '_']
letras_erradas = []

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while (not acertou and not enforcou):
    chute = input('Qual a letra? ')
    posicao = 0
    if chute.upper() in palavra_secreta.upper():
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1
        letras_erradas.append(chute)
    print('Letras erradas: ',letras_erradas)
    print('palavra: ')
    print(letras_acertadas)
    
    acertou = '_' not in letras_acertadas
    enforcou = erros == 8
if acertou:
    print('Você Ganhou!')
else:
    print('você perdeu...')

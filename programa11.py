# programa lê quatro notas e mostra na tela a média entre elas

notas = []
soma = 0
for a in range(1, 5):
    nota = float(input('Informe a {}ª nota:\n'.format(a)))
    notas.append(nota)
for b in range(0, len(notas)):
    soma += notas[b]
media = soma/len(notas)
print('A média vale: {:.2f}'.format(media))

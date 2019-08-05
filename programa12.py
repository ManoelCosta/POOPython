# programa le dados do usuario, armazena num dict() e imprime os valores na tela

pessoa = {'Nome': '', 'Idade': '', 'Cidade': ''}

pessoa['Nome'] = input('Informe o seu nome:\n')
pessoa['Idade'] = int(input('Informe a idade:\n'))
pessoa['Cidade'] = input('Informe sua cidade:\n')

print('Nome:', pessoa['Nome'])
print('Idade:', pessoa['Idade'])
print('Cidade:', pessoa['Cidade'])

# programa le dados do usuario, armazena num dict() e imprime os valores na tela

dados_do_usuario = {'Nome': '', 'Idade': '', 'Cidade': ''}

dados_do_usuario['Nome'] = input('Informe o seu nome:\n')
dados_do_usuario['Idade'] = int(input('Informe a idade:\n'))
dados_do_usuario['Cidade'] = input('Informe sua cidade:\n')

print('Nome:', dados_do_usuario['Nome'])
print('Idade:', dados_do_usuario['Idade'])
print('Cidade:', dados_do_usuario['Cidade'])

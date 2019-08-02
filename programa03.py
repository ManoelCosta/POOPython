from datetime import date
nome = input('Informe seu nome:\n')
ano_nascimento = int(input('Informe o ano de nascimento:\n'))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print('Seu nome é {} e sua idade é {}'.format(nome, idade))

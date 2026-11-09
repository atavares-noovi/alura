#Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade = int(input('qual a sua idade: '))

if idade >= 0 and idade <= 12:
    print('um nenem')
elif idade >= 13 and idade <= 17:
    print ('um bicho do mato')
else:
    print ('maior de idade')
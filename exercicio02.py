#2. Faça um programa que verifique a senha e o login de um sistema e só finalize quando ele acertar os dados.  Considere: login = "tds01" | senha = "123"

print('É necessário fazer o Login para seguir')


usuario = input('Nome de usuário: ')
senha = input('Digite a senha: ')

if usuario == "tds01":
    if senha == "123":
        print("Acesso liberado!")
    else:
        print("Usuário ou senha incorretos!")

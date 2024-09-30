'''3. Com base no exercício  anterior, limite o usuário a apenas 3 tentativas até acertar, se ele não acertar deve mostrar "senha bloqueada"
'''


print('É necessário fazer o Login para seguir')

usuario = input('Nome de usuário: ')
tentativas = 0

if usuario == "tds01":
    while tentativas < 3:
        senha = input('Digite a senha: ')
        
        if senha == "123":
            print("Acesso liberado!")
        else:
            tentativas += 1
            print(f"Usuário ou senha incorretos! Tentativa {tentativas} de 3.")
    
    if tentativas == 3:
        print("Senha bloqueada.")
else:
    print("Usuário não encontrado!")


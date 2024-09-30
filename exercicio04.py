candidato = 0
jair = 0
carlos = 0
neves = 0
nulo = 0 
branco = 0
print('Urna de voto eletrônico. Escolha uma opção a seguir: \n')
print('1 - Jair Rodrigues \n')
print('2 - Carlos Luz \n')
print('3 - Neves Rocha \n')
print('4 - Nulo \n')
print('5 - Branco \n')

while True:
    candidato = int(input('Digite o número do seu candidato. Digite 6 para mais opções. \n')) 
    if candidato == 1:
        jair += 1
        print("Candidato escolhido: Candidato Jair")
    elif candidato == 2:
        carlos += 1
        print("Candidato escolhido: Candidato Carlos")
    elif candidato == 3:
        neves += 1
        print("Candidato escolhido: Candidato Neves")
    elif candidato == 4:
        nulo += 1
        print("Você votou Nulo")
    elif candidato == 5:
        branco += 1
        print("Você votou em Branco")
    elif candidato == 6:
        print("Resultado da votação:")
        print("Saldo de votos do Jair:", jair)
        print("Saldo de votos do Carlos:", carlos)
        print("Saldo de votos do Neves:", neves)
        print("Saldo de votos Nulos:", nulo)
        print(nulo/(jair+carlos+neves+nulo+branco)*100,"%")
        print("Saldo de votos Brancos:", branco)
        print(branco/(jair+carlos+neves+nulo+branco)*100,"%")
    else:
        print("Opção inválida! Tente novamente.")
    
 
canditadoHamburguer = 0
canditadoPizza = 0
votoNulo = 0

print('Para iniciar a urna digite 140 e para encerrar digite 160 \n')

voto = int(input('Iniciar a urna: '))
print('\n')

while voto < 150:
    
    voto = 0
    print('Escolha qual candidato você irá votar: \n')
    print('Para candidato HAMBURGUER digite 1')
    print('Para candidato PIZZA digite 8')
    print('Voto nulo digite 100 \n')
    voto = int(input('Digite seu voto: '))
    if voto == 1:
        canditadoHamburguer = canditadoHamburguer + 1
    elif voto == 8:
        canditadoPizza = canditadoPizza + 1
    elif voto == 100:
        votoNulo = votoNulo + 1
    print ('Voto confirmado! \n')
    print('------------------------------------------------------------------')
else:
    print ('Sessão encerrada! \n')
    print('O candidato HAMBURGUER recebeu ', canditadoHamburguer,' votos')
    print('O candidato PIZZA recebeu ', canditadoPizza,' votos')
    print('Votos nulos e brancos ', votoNulo)

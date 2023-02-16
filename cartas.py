import random

posibilidades=('A','J', 'Q', 'K','2', '3', '4', '5', '6', '7', '8', '9', '10')
baraja=[]

for i in range(52):
    baraja.append(random.choice(posibilidades))

baraja_tuple=tuple(baraja)
print(baraja_tuple)
print()

def juego(baraja_tuple):
    player1 = 0
    player2 = 0
    for i in range (0,52,8):
        if baraja_tuple[i] == "A":
            player1 += 1
        if baraja_tuple[i] == "J":
            player1 += 2
        if baraja_tuple[i] == "Q":
            player1 += 3
        if baraja_tuple[i] == "K":
            player1 += 4
    for i in range (4,52,8):
        if baraja_tuple[i] == "A":
            player2 += 1
        if baraja_tuple[i] == "J":
            player2 += 2
        if baraja_tuple[i] == "Q":
            player2 += 3
        if baraja_tuple[i] == "K":
            player2 += 4
    return player1,player2

print(juego(baraja_tuple))
print()

def cartas_siguientes():
    return baraja_tuple[1:4]

print(cartas_siguientes())

def tiene_cartas_altas(cartas_siguientes):
    if "Q" in cartas_siguientes() or "A" in cartas_siguientes() or "J" in cartas_siguientes() or "K" in cartas_siguientes():
        return(True)
    else:
        return(False)

print(tiene_cartas_altas(cartas_siguientes))
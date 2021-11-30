laberinto = [
    ['a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a'],
    ['a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a']
    ]
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

def es_muro(numA, numB):
    for i in range(len(muro)):
        #print("índice i del laberinto = " + str(numA) + "índice j del laberinto = " + str(numB) + "valor i del muro = " + str(muro[i][0]) + "valor i del muro = " + str(muro[i][1]))
        if muro[i][0] == numA and muro[i][1] == numB:
            return True

    return False


for i in range(len(laberinto)):
    for j in range(len(laberinto[0])):
        #print(str(i) + ' ' + str(j))
        if es_muro(i, j) == True: 
            laberinto[i][j] = 'X'
        else:
            laberinto[i][j] = ' '
laberinto[4][4] = 'S'

for i in range(len(laberinto)):
    print(laberinto[i])
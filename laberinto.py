laberinto = [
    ['a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a'],
    ['a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a'], 
    ['a', 'a', 'a', 'a', 'a']
    ]
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
camino = []
visitadas = []
solucion = []


def meterEnLista(numA, numB, lista):
    par = []
    par.append(numA)
    par.append(numB)
    lista.append(par)

def estaEnLista(numA, numB, lista):
    for i in range(len(lista)):
        #print("índice i del laberinto = " + str(numA) + "índice j del laberinto = " + str(numB) + "valor i del muro = " + str(muro[i][0]) + "valor i del muro = " + str(muro[i][1]))
        if lista[i][0] == numA and lista[i][1] == numB:
            return True

    return False


def init_laberinto():
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            #print(str(i) + ' ' + str(j))
            if estaEnLista(i, j, muro) == True: 
                laberinto[i][j] = 'X'
            else:
                laberinto[i][j] = ' '
    laberinto[4][4] = 'S'



def init_camino():
    for i in range(len(laberinto)):
        for j in range(len(laberinto)):
            if laberinto[i][j] == ' ':
                meterEnLista(i, j, camino)
            elif laberinto[i][j] == 'S':
                meterEnLista(i, j, camino)

    
    


       

init_laberinto()
init_camino()

for i in range(len(laberinto)):
    print(laberinto[i])

print(camino)
            

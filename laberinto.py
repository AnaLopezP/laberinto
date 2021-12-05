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


def arriba(i, j):
    if i > 0 and i < 5:
        if laberinto[i-1][j] != "X":
            if estaEnLista(i-1, j, visitadas) == False:
                return True
    return False

def abajo(i, j):
    if i >= 0 and i < 4:
        if laberinto[i+1][j] != "X":
            if estaEnLista(i+1, j, visitadas) == False:
                return True
    return False

def derecha(i, j):
    if j >= 0 and j < 4:
        if laberinto[i][j+1] != "X":
            if estaEnLista(i, j+1, visitadas) == False:
                return True
    return False

def izquierda(i, j):
    if j > 0 and j <= 5:
        if laberinto[i][j-1] != "X":
            if estaEnLista(i, j-1, visitadas) == False:
                return True
    return False

def calcular_siguiente(posicion_actual):
    coordenada = []
    i = posicion_actual[0]
    j = posicion_actual[1]
    if arriba(i, j) == True:
        solucion.append("Arriba")
        coordenada.append(i-1)
        coordenada.append(j)
    elif abajo(i, j) == True:
        solucion.append("Abajo")
        coordenada.append(i+1)
        coordenada.append(j)
    elif izquierda(i, j) == True:
        solucion.append("Izquierda")
        coordenada.append(i)
        coordenada.append(j-1)
    elif derecha(i, j) == True:
        solucion.append("Derecha")
        coordenada.append(i)
        coordenada.append(j+1)
    return coordenada
    


       

init_laberinto()
init_camino()

for i in range(len(laberinto)):
    print(laberinto[i])

print(camino)

posicion_actual = [0,0]
i = posicion_actual[0]
j = posicion_actual[1]
while laberinto[i][j] != "S":
    posicion_siguiente = calcular_siguiente(posicion_actual)
    meterEnLista(posicion_actual[0], posicion_actual[1], visitadas)
    posicion_actual[0] = posicion_siguiente[0]
    posicion_actual[1] = posicion_siguiente[1]
    i = posicion_actual[0]
    j = posicion_actual[1]

print(solucion)
print("fin")
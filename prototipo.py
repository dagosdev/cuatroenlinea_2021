def tableroVacio():
    return [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            ]

def contenidoColumna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda)
    return columna


def completarTableroEnOrden(secuencia, tablero):
    for indice, columna in enumerate(secuencia):
        fichaNumero = 1 + (indice % 2)
        soltarFichaEnColumna(fichaNumero, columna, tablero)
    return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return

def dibujarTablero(tablero):
    for fila in tablero:
        for celda in fila:
            if celda == 0:
                print('   ', end='')
            else:
                print(' %s ' % celda, end='')
        print('')



def secuenciaValida(secuencia):
    for columna in secuencia:
        if columna < 1 or columna > 7:
            return False
    return True

secuencia_texto = input("Ingrese la secuencia de numeros: ")
secuencia = []
for items in secuencia_texto.split(','):
    secuencia.append(int(items))

tablero = []
if secuenciaValida(secuencia):
    tablero = completarTableroEnOrden(secuencia, tableroVacio())
    dibujarTablero(tablero)
else:
    print("Las columnas deberian ir de 1 al 7")


print(contenidoColumna(1, tablero))


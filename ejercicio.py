N = 9
MINIMO = 23
 
laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1],
]
 
MOVIMIENTOS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
 
INICIO = (8, 0)
FIN = (0, 0)
 
 
def valor(f, c):
    v = laberinto[f][c]
    if v == 'I' or v == 'F':
        return 1
    return v
 
 
def puede_pasar(f, c, camino):
    if f < 0 or f >= N or c < 0 or c >= N:
        return False
    if valor(f, c) == 0:
        return False
    if camino[f][c] != 0:
        return False
    return True
 
 
def buscar(f, c, puntos, camino, paso):
    camino[f][c] = paso
    puntos = puntos + valor(f, c)
 
    if (f, c) == FIN:
        if puntos >= MINIMO:
            return True
        camino[f][c] = 0
        return False
 
    for df, dc in MOVIMIENTOS:
        nf = f + df
        nc = c + dc
        if puede_pasar(nf, nc, camino):
            if buscar(nf, nc, puntos, camino, paso + 1):
                return True
 
    camino[f][c] = 0
    return False
 
 
def mostrar_laberinto():
    for fila in laberinto:
        for x in fila:
            print(f"{str(x):>3}", end="")
        print()
 
 
def mostrar_camino(camino):
    for fila in camino:
        for x in fila:
            print(f"{x:>3}", end="")
        print()
 
 
def sumar_puntos(camino):
    total = 0
    for f in range(N):
        for c in range(N):
            if camino[f][c] != 0:
                total = total + valor(f, c)
    return total
 
 
def main():
    print("LABERINTO")
    mostrar_laberinto()
    print()
 
    camino = []
    for i in range(N):
        camino.append([0] * N)
 
    if buscar(INICIO[0], INICIO[1], 0, camino, 1):
        print("El raton salio del laberinto")
        print("Puntos:", sumar_puntos(camino), "(minimo", MINIMO, ")")
        print("Camino (el numero es el orden de los pasos):")
        mostrar_camino(camino)
    else:
        print("El raton no pudo salir del laberinto")
 
 
main()
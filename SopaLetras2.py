import random

def generar_sopa_letras(tamaño):
    letras = [chr(random.randint(65, 90)) for _ in range(tamaño * tamaño)]  # Genera letras aleatorias en mayúsculas
    sopa_letras = [letras[i:i+tamaño] for i in range(0, len(letras), tamaño)]  # Crea la cuadrícula
    return sopa_letras

def imprimir_sopa_letras(sopa_letras):
    tamaño = len(sopa_letras)
    for i in range(tamaño):
        for j in range(tamaño):
            print(sopa_letras[i][j], end=" ")
        print()

def ocultar_palabras(sopa_letras, palabras, cantidad_palabras_mostrar):
    palabras_ocultar = random.sample(palabras, cantidad_palabras_mostrar)  # Selecciona palabras al azar para ocultar
    for palabra in palabras_ocultar:
        if len(palabra) <= len(sopa_letras):
            direccion = random.choice(["horizontal", "vertical", "diagonal"])
            if direccion == "horizontal":
                fila = random.randint(0, len(sopa_letras) - 1)
                columna = random.randint(0, len(sopa_letras) - len(palabra))
                for i in range(len(palabra)):
                    sopa_letras[fila][columna + i] = palabra[i]
            elif direccion == "vertical":
                fila = random.randint(0, len(sopa_letras) - len(palabra))
                columna = random.randint(0, len(sopa_letras) - 1)
                for i in range(len(palabra)):
                    sopa_letras[fila + i][columna] = palabra[i]
            elif direccion == "diagonal":
                fila = random.randint(0, len(sopa_letras) - len(palabra))
                columna = random.randint(0, len(sopa_letras) - len(palabra))
                for i in range(len(palabra)):
                    sopa_letras[fila + i][columna + i] = palabra[i]

def buscar_palabra(sopa_letras, palabra):
    tamaño = len(sopa_letras)
    for i in range(tamaño):
        for j in range(tamaño):
            if sopa_letras[i][j] == palabra[0]:
                if buscar_en_direccion(sopa_letras, palabra, i, j):
                    return True
    return False

def buscar_en_direccion(sopa_letras, palabra, fila, columna):
    direcciones = [(0, 1), (1, 0), (1, 1), (1, -1)]  # Horizontal, vertical, diagonal ascendente, diagonal descendente
    for direccion in direcciones:
        dx, dy = direccion
        encontrada = True
        for letra in palabra[1:]:
            fila += dx
            columna += dy
            if fila < 0 or fila >= len(sopa_letras) or columna < 0 or columna >= len(sopa_letras) or sopa_letras[fila][columna] != letra:
                encontrada = False
                break
        if encontrada:
            return True
    return False

def main():
    tamaño_sopa = 8
    cantidad_palabras_mostrar = 3  # Número de palabras a mostrar
    palabras = ["GATO","PERRO","RATON","SAPO","VACA","TORO"]
    sopa_letras = generar_sopa_letras(tamaño_sopa)
    ocultar_palabras(sopa_letras, palabras, cantidad_palabras_mostrar)
    palabras_encontradas = []

    while True:
        imprimir_sopa_letras(sopa_letras)
        fila = int(input("Ingresa la fila: "))
        columna = int(input("Ingresa la columna: "))
        palabra = input("Ingresa la palabra a buscar: ").upper()

        if buscar_palabra(sopa_letras, palabra):
            print("¡Encontraste la palabra!")
            palabras_encontradas.append(palabra)
        else:
            print("La palabra no se encontró.")

        respuesta = input("¿Quieres seguir buscando? (Sí/No): ").lower()
        if respuesta != "si":
            break

    print("Palabras encontradas:")
    for palabra in palabras_encontradas:
        print(palabra)

if __name__ == "__main__":
    main()

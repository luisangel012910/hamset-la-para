import random
import string
import time

abecedario = list(string.ascii_uppercase)
animales = ['TIGRE', 'RATON', 'PERRO', 'GATO', 'LORO', 'PEZ']
sopa = []

def jugar_palabras(sopa, palabras_seleccionadas, tiempo_limite):
    print("Bienvenido al juego de encontrar palabras en la sopa de letras.")
    print("Encuentra las siguientes palabras en la sopa de letras:")
    imprimir_matriz(sopa, 2)
    print(f"Tienes {tiempo_limite} segundos para encontrar todas las palabras.")
    print("Escribe 'salir' para terminar el juego.")
    
    palabras_restantes = list(palabras_seleccionadas)  # Hacemos una copia de las palabras seleccionadas
    tiempo_inicio = time.time()
    
    while palabras_restantes:
        tiempo_transcurrido = time.time() - tiempo_inicio
        tiempo_restante = max(0, tiempo_limite - tiempo_transcurrido)
        
        if tiempo_restante == 0:
            print("¡Tiempo agotado! Has excedido el tiempo límite.")
            return
        
        palabra_usuario = input(f"Tienes {int(tiempo_restante)} segundos restantes. Escribe una palabra encontrada: ").strip().upper()
        
        if palabra_usuario == 'SALIR':
            print("Gracias por jugar. ¡Hasta luego!")
            return
        
        if palabra_usuario in palabras_restantes:
            if verificar_palabra(sopa, palabra_usuario):
                print("¡Felicidades! Encontraste la palabra", palabra_usuario)
                palabras_restantes.remove(palabra_usuario)
            else:
                print("La palabra", palabra_usuario, "no está en la sopa de letras.")
        else:
            print("La palabra", palabra_usuario, "no es una de las palabras a encontrar.")
    
    print("¡Has encontrado todas las palabras! ¡Felicidades!")

def rellenar_sopa(sopa, tam):
    for i in range(tam):
        fila_temp = []
        for j in range(tam):
            fila_temp.append(abecedario[random.randint(0, 25)])
        sopa.append(fila_temp)

def imprimir_matriz(M, tam_max):
    print(" ".rjust(tam_max), end="")
    for i in range(1, len(M) + 1):
        print(str(i).rjust(tam_max), end=' ')
    print()
    i = 1
    for fila in M:
        print(i, end=" ")
        i += 1
        for elemento in fila:
            print(str(elemento).rjust(tam_max), end=' ')
        print()

def elegir_palabras(tematica, cant):
    palabras_elegidas = random.sample(tematica, cant)
    return palabras_elegidas

def incluir_palabras(sopa, palabras):
    for palabra in palabras:
        direccion = random.randint(0, 1)  # 0 para horizontal, 1 para vertical
        tampal = len(palabra)
        tam = len(sopa)
        if direccion == 0:  # Horizontal
            horizontal(sopa, palabra, tam, tampal)
        else:  # Vertical
            vertical(sopa, palabra, tam, tampal)

def horizontal(sopa, palabra, tam, tampal):
    x = random.randint(0, tam - 1)
    y = random.randint(0, tam - 1)
    while y + tampal > tam:
        y = random.randint(0, tam - 1)
    for i in range(tampal):
        sopa[x][y + i] = palabra[i]

def vertical(sopa, palabra, tam, tampal):
    x = random.randint(0, tam - 1)
    y = random.randint(0, tam - 1)
    while x + tampal > tam:
        x = random.randint(0, tam - 1)
    for i in range(tampal):
        sopa[x + i][y] = palabra[i]

def verificar_palabra(sopa, palabra):
    tam = len(sopa)
    
    # Verificar horizontalmente
    for fila in sopa:
        fila_actual = ''.join(fila)
        if palabra.lower() in fila_actual.lower():
            return True
    
    # Verificar verticalmente
    for j in range(len(sopa[0])):
        columna_actual = ''.join([sopa[i][j] for i in range(len(sopa))])
        if palabra.lower() in columna_actual.lower():
            return True
    
    # Verificar en diagonal (de izquierda a derecha y de arriba hacia abajo)
    for i in range(tam):
        for j in range(tam):
            if i + len(palabra) <= tam and j + len(palabra) <= tam:
                diagonal = ''.join([sopa[i + k][j + k] for k in range(len(palabra))])
                if palabra.lower() in diagonal.lower():
                    return True

    # Verificar en diagonal (de derecha a izquierda y de arriba hacia abajo)
    for i in range(tam):
        for j in range(tam):
            if i + len(palabra) <= tam and j - len(palabra) >= -1:
                diagonal = ''.join([sopa[i + k][j - k] for k in range(len(palabra))])
                if palabra.lower() in diagonal.lower():
                    return True
    
    return False

# Modificar el tamaño de la sopa según sea necesario
tam_sopa = 8

rellenar_sopa(sopa, tam_sopa)
palabras_seleccionadas = elegir_palabras(animales, 3)
incluir_palabras(sopa, palabras_seleccionadas)

# Definir el tiempo límite en segundos
tiempo_limite = 120

# Iniciar el juego
jugar_palabras(sopa, palabras_seleccionadas, tiempo_limite)

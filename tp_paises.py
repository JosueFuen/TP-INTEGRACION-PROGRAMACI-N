import csv
import os
NOMBRE_ARCHIVO='country_data.csv'
opcion=''
#Argentina,45376763,2780400,América
if not os.path.exists(NOMBRE_ARCHIVO):
    with open (NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=['nombre','poblacion','superficie','continente'])
        escritor.writeheader()
#Crea una lista de diccionarios con la informacion de los paises
def catalogo_paises():
    paises=[]
    with open (NOMBRE_ARCHIVO, newline='', encoding='utf-8' ) as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            paises.append({'nombre':fila['nombre'], 'poblacion':int(fila['poblacion']),'superficie':int (fila['superficie']),'continente':fila['continente']})
        return paises
    
#De ahora en mas, vamos a trabajar con 'paises'en lugar de la funcion 'catalogo_paises'
DATOS_PAISES=catalogo_paises()

def menu():
    print("\n             MENÚ  ")
    print("1)   Agregar país")
    print("2)   Actualizar datos")
    print("3)   Buscar país")
    print("4)   Filtrar países")
    print("5)   Ordenar países")
    print("6)   Mostrar estadísticas")
    print("7)   Salir")

    
#Crea una lista a partir del catalogo de paises. Esto sirve para validar textos. En este caso podemos
# seleccionar nombre o continente.
def lista_territorio (territorio):
    lista=[]
    #Tuvimos que agregar este if, debido a que en el catalogo, el encabezado se llama nombre. 
    #La otra solucion era cambiar el encabezado por 'pais', asi quedaba todo mas fluido y sin 
    # complicaciones, pero la consigna indica que se llame 'nombre'
    if territorio=='pais':
        clave='nombre'
    else:
        clave='continente'

    for pais in DATOS_PAISES:
        lista.append(pais[f'{clave}'].lower())
    return lista

#Valida que el pais no exista o que no se ingrese nada
def validacion_pais():
    nombre_pais=input('Ingrese el nombre del país: ').strip()
    lista=lista_territorio('pais')
    while True:
        if nombre_pais.lower() in lista:
            nombre_pais=input("====== ERROR ======\nEl pais ingresado ya existe. Intente con otro: ").strip()
            continue
        elif nombre_pais=='':
            nombre_pais=input("====== ERROR ======\nNo ha ingresado ningún pais. Intente nuevamente: ").strip()
            continue
        break
    return nombre_pais

#Valida los digitos de poblacion o superficie a eleccion
def validacion_digitos(tipo):
    print('='*60)
    cantidad=input(f"Ingrese la {tipo} del país: ").strip()
    while True:
        if not cantidad.isdigit() or cantidad =='':
            cantidad=input("====== ERROR ======\nDebe ingresa un digito. Intente nuevamente: ").strip()
            continue
        cantidad=int(cantidad)
        if cantidad<1:
            cantidad=input(f"====== ERROR ======\nDebe ingresar un digito mayor a cero. Intente nuevamente: ").strip()
            continue
        return cantidad
#Te hace elegir entre las opciones de continente, para que no haya ningun error
def validacion_continente():
    print('-----CONTINENTE PARA ELEGIR-----')
    print('1) África')
    print('2) América')
    print('3) Asia')
    print('4) Europa')
    print('5) Oceanía')
    while True:
        option=input('Indique el continente: ').strip()
        match option:
            case '1':
                nombre_continente='África'
                break
            case '2':
                nombre_continente='América'
                break
            case '3':
                nombre_continente='Asia'
                break
            case '4':
                nombre_continente='Europa'
                break
            case '5':
                nombre_continente='Oceanía'
                break
            case _:
                pausa=input('Opción incorrecta. Intente de nuevo.')
                continue
    return nombre_continente

#Compara que el pais indicado se encuentre dentro de la lista de paises. Ademas chequea 
# que el pais exista y que no este vacio
def buscar_pais():
    nombre_pais=input('Ingrese el nombre del país: ').strip()
    lista_paises=lista_territorio('pais')
    while True:
        if nombre_pais.lower() not in lista_paises:
            nombre_pais=input('El pais ingresado no existe. Intente nuevamente: ')
            continue
        elif nombre_pais=='':
            nombre_pais=input('Debe ingresar un nombre. Intente nuevamente: ')
            continue
        break
    return nombre_pais

#filtra los paises por continente seleccionado
def filtro_continente():
    nombre_continente=validacion_continente()
    paises_filtrados=[]
    for datos_pais in DATOS_PAISES:
        if nombre_continente==datos_pais['continente']:
            paises_filtrados.append(datos_pais)
    print(paises_filtrados)
    return paises_filtrados

#Es una validación de que el numero ingresado es un digito. Es casi la misma funcion que la validacion_digito, 
# pero esta no tiene ningun input
def validacion_rango_digito(rango):
    while True:
        if not rango.isdigit() or rango =='':
            rango=input("====== ERROR ======\nDebe ingresa un digito. Intente nuevamente: ").strip()
            continue
        rango=int(rango)
        if rango<1:
            rango=input(f"====== ERROR ======\nDebe ingresar un digito mayor a cero. Intente nuevamente: ").strip()
            continue
        return rango

def filtro_rangos(tipo):
    rango_superior=input('Ingrese el rango superior para el filtro: ').strip()
    rango_superior=validacion_rango_digito(rango_superior)
    rango_inferior=input('Ingrese el rango inferior para el filtro: ').strip()
    rango_inferior=validacion_rango_digito(rango_inferior)

    paises_filtrados=[]
    for datos_pais in DATOS_PAISES:
        if datos_pais[tipo]<=rango_superior and datos_pais[tipo]>=rango_inferior:
            paises_filtrados.append(datos_pais)
    print (paises_filtrados)
    return paises_filtrados




#función principal para agregar un nuevo país.
def agregar_pais():
    nombre_pais=validacion_pais()
    poblacion=validacion_digitos('poblacion')
    superficie=validacion_digitos('superficie')
    nombre_continente=validacion_continente()
    nuevo_pais={'nombre':nombre_pais,'poblacion':poblacion,'superficie':superficie,'continente':nombre_continente}

    with open (NOMBRE_ARCHIVO, 'a', newline='', encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo,fieldnames=['nombre','poblacion','superficie','continente'])
        escritor.writerow(nuevo_pais)
    DATOS_PAISES.append(nuevo_pais)
    return

#funcion principal actualizar datos
def actualizar_datos():
    if not DATOS_PAISES:
        pausa=input('Todavía no se ha cargado ningún dato al archivo. Presione enter para continuar.')
        return
    nombre_pais=buscar_pais()
    poblacion=validacion_digitos('poblacion')
    superficie=validacion_digitos('superficie')
    for datos_pais in DATOS_PAISES:
        if nombre_pais.lower()== datos_pais['nombre'].lower():
            datos_pais['poblacion']=poblacion
            datos_pais['superficie']=superficie
            break
    with open (NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=['nombre','poblacion','superficie','continente'])
        escritor.writeheader()
        escritor.writerows(DATOS_PAISES)
#Busca el pais por palabra ingresada 
def buscar_pais_palabra():
    nombre_pais=input('Ingresar nombre de pais: ').strip()
    while True:
        if nombre_pais=='':
            nombre_pais=input('Debe ingresar una palabra clave. Intente nuevamente: ').strip()
            continue
        break
    paises_filtrados=[]
    for fila in DATOS_PAISES:
        if nombre_pais.lower() in fila['nombre'].lower():
            paises_filtrados.append(fila)
    print(paises_filtrados)
    pausa=input('Presione enter para continuar: ')

def filtrar_pais():
    print('Filtrar paises por: ')
    print('1) Continente')
    print('2) Rango de población')
    print('3) Rango de superficie')
    print('4) Volver atras')
    option=''
    while option!='4':
        option=input('Ingrese la opción deseada:')
        match option:
            case '1':
                filtro_continente()
                break
            case '2':
                filtro_rangos('poblacion')
                break
            case '3':
                filtro_rangos('superficie')
                break
            case '4':
                break
            case _:
                pausa=input('Opción incorrecta. Intente nuevamente.')
                continue

# ------------------------------------------------------------
# Ordenar paises
#funcion principal para ordenar los paises por nombre, poblacion o superficie

def ordenar_paises():
    while True:
        print('')
        print('Ordenar paises por: ')
        print('1) Nombre')
        print('2) Poblacion')
        print('3) Superficie')
        print('4) Volver atras')
        option=input('Ingrese la opción deseada:').strip()
        match option:
            case '1':
                ordenar_por_nombre()
            case '2':
                ordenar_por_poblacion()
            case '3':
                ordenar_por_superficie()
            case '4':
                break
            case _:
                print('Opción incorrecta. Intente nuevamente.')

# Funcion generica de ordenamiento burbuja (Bubble Sort)
# Recibe la lista de paises, el campo por el cual ordenar, y si es ascendente o descendente
def bubble_sort_paises(paises, campo, ascendente=True):
    """
    Ordena una lista de paises usando el algoritmo Bubble Sort.

    Parametros:
    - paises: lista de diccionarios con datos de paises
    - campo: 'nombre', 'poblacion' o 'superficie'
    - ascendente: True para orden ascendente, False para descendente

    Retorna: lista ordenada (no modifica la lista original)
    """
    # Hacemos una copia para no modificar la lista original
    paises_ordenados = paises.copy()
    n = len(paises_ordenados)

    # Si hay menos de 2 elementos, ya esta ordenado
    if n < 2:
        return paises_ordenados

    # Algoritmo Bubble Sort
    for i in range(n - 1):
        # Bandera para optimizar: si no hay intercambios, la lista ya esta ordenada
        intercambio_realizado = False

        for j in range(n - 1 - i):
            # Obtenemos los valores a comparar
            if campo == 'nombre':
                valor_actual = paises_ordenados[j][campo].lower()
                valor_siguiente = paises_ordenados[j + 1][campo].lower()
            else:
                valor_actual = paises_ordenados[j][campo]
                valor_siguiente = paises_ordenados[j + 1][campo]

            # Comparacion segun el orden deseado
            if ascendente:
                # Orden ascendente: si el actual es mayor que el siguiente, intercambiar
                debe_intercambiar = valor_actual > valor_siguiente
            else:
                # Orden descendente: si el actual es menor que el siguiente, intercambiar
                debe_intercambiar = valor_actual < valor_siguiente

            if debe_intercambiar:
                # Intercambiar los elementos
                paises_ordenados[j], paises_ordenados[j + 1] = paises_ordenados[j + 1], paises_ordenados[j]
                intercambio_realizado = True

        # Si no hubo intercambios en esta pasada, la lista ya esta ordenada
        if not intercambio_realizado:
            break

    return paises_ordenados

# Funcion para mostrar paises formateados
def mostrar_paises_formateados(paises):
    """
    Muestra la lista de paises en formato de tabla
    Parametros:
    - paises: lista de diccionarios con datos de paises
    """
    if not paises:
        print("No hay paises para mostrar.")
        return

    print('\n' + '--'*50)
    print(f"{'Nombre':<20} | {'Poblacion':>15} | {'Superficie':>18} | {'Continente':<15}")
    print('--'*50)
    for pais in paises:
        print(f"{pais['nombre']:<20} | {pais['poblacion']:>15,} | {pais['superficie']:>15,} km | {pais['continente']:<15}")
    print('--'*50)

# Funcion para ordenar por nombre
def ordenar_por_nombre():
    if not tiene_paises():
        return

    print('Ordenar paises por nombre:')
    print('1) Ascendente (A-Z)')
    print('2) Descendente (Z-A)')
    opcion_orden = input('Seleccione el orden: ').strip()

    ascendente = (opcion_orden == '1')

    paises_ordenados = bubble_sort_paises(DATOS_PAISES, 'nombre', ascendente)

    print(f'Paises ordenados por nombre ({("ascendente" if ascendente else "descendente")}):')
    mostrar_paises_formateados(paises_ordenados)
    input('Presione enter para continuar: ')

# Funcion para ordenar por poblacion
def ordenar_por_poblacion():
    if not tiene_paises():
        return

    print('Ordenar paises por poblacion:')
    print('1) Ascendente (menor a mayor)')
    print('2) Descendente (mayor a menor)')
    opcion_orden = input('Seleccione el orden: ').strip()

    ascendente = (opcion_orden == '1')

    paises_ordenados = bubble_sort_paises(DATOS_PAISES, 'poblacion', ascendente)

    print(f'Paises ordenados por poblacion ({("ascendente" if ascendente else "descendente")}):')
    mostrar_paises_formateados(paises_ordenados)
    input('Presione enter para continuar: ')

# Funcion para ordenar por superficie
def ordenar_por_superficie():
    if not tiene_paises():
        return

    print('Orden:')
    print('1) Ascendente (menor a mayor)')
    print('2) Descendente (mayor a menor)')
    opcion_orden = input('Seleccione el orden: ').strip()

    ascendente = (opcion_orden == '1')

    paises_ordenados = bubble_sort_paises(DATOS_PAISES, 'superficie', ascendente)

    print(f'Paises ordenados por superficie ({("ascendente" if ascendente else "descendente")}):')
    mostrar_paises_formateados(paises_ordenados)
    input('Presione enter para continuar: ')

# Fin ordenar paises
# ------------------------------------------------------------

# ------------------------------------------------------------
# Mostrar estadisticas
#funcion principal para mostrar el pais con mayor y menor poblacion
def mayor_menor_poblacion():
    """
    Muestra el pais con mayor y menor poblacion
    Parametros:
    - DATOS_PAISES: lista de diccionarios con datos de paises
    """
    # validar si hay paises para mostrar
    if not tiene_paises():
        return

    # inicializar variables
    mayor_poblacion= DATOS_PAISES[0]
    menor_poblacion= DATOS_PAISES[0]

    # recorrer la lista de paises para encontrar el pais con mayor y menor poblacion
    for datos_pais in DATOS_PAISES:
        # si encontramos un pais con mayor poblacion, actualizamos la variable
        if datos_pais['poblacion'] > mayor_poblacion['poblacion']:
            mayor_poblacion=datos_pais

        # si encontramos un pais con menor poblacion, actualizamos la variable
        if datos_pais['poblacion'] < menor_poblacion['poblacion']:
            menor_poblacion=datos_pais

    # mostrar los paises con mayor y menor poblacion
    print('')
    print ('--'*50)
    print ('Paises con mayor y menor poblacion: ')
    print ('--'*50)
    print ('Pais con mayor poblacion:')
    print (f'Nombre: {mayor_poblacion['nombre']}')
    print (f'Poblacion: {mayor_poblacion['poblacion']}')
    print (f'Superficie: {mayor_poblacion['superficie']} km')
    print (f'Continente: {mayor_poblacion['continente']}')
    print ('--'*50)
    print ('Pais con menor poblacion:')
    print (f'Nombre: {menor_poblacion['nombre']}')
    print (f'Poblacion: {menor_poblacion['poblacion']}')
    print (f'Superficie: {menor_poblacion['superficie']} km')
    print (f'Continente: {menor_poblacion['continente']}')
    print ('--'*50)
    print('')
    input('Presione enter para continuar: ')
    return

# funcion promedio de poblacion
def promedio_poblacion():
    """
    Muestra el promedio de poblacion de los paises
    Parametros:
    - DATOS_PAISES: lista de diccionarios con datos de paises
    """
    # validar si hay paises para mostrar
    if not tiene_paises():
        return

    # inicializar variable
    suma_poblacion=0
    # calcular el promedio de poblacion
    for datos_pais in DATOS_PAISES:
        suma_poblacion+=datos_pais['poblacion']
    promedio_poblacion=suma_poblacion / len(DATOS_PAISES)
    print('')
    print('--'*50)
    print(f'Promedio de poblacion: {promedio_poblacion:.2f}')
    print('--'*50)
    print('')
    return

# funcion promedio de superficie
def promedio_superficie():
    """
    Muestra el promedio de superficie de los paises
    Parametros:
    - DATOS_PAISES: lista de diccionarios con datos de paises
    """
    # validar si hay paises para mostrar
    if not tiene_paises():
        return

    # inicializar variable
    suma_superficie=0
    # calcular el promedio de superficie
    for datos_pais in DATOS_PAISES:
        suma_superficie+=datos_pais['superficie']
    promedio_superficie=suma_superficie / len(DATOS_PAISES)
    print('')
    print('--'*50)
    print(f'Promedio de superficie: {promedio_superficie:.2f}')
    print('--'*50)
    print('')
    return

# funcion cantidad de paises por continente
def cantidad_paises_continente():
    """
    Muestra la cantidad de paises por continente
    Parametros:
    - DATOS_PAISES: lista de diccionarios con datos de paises
    """
    # validar si hay paises para mostrar
    if not tiene_paises():
        return
    paises_por_continente={}

    for datos_pais in DATOS_PAISES:
        if datos_pais['continente'] not in paises_por_continente:
            paises_por_continente[datos_pais['continente']]=1
        else:
            paises_por_continente[datos_pais['continente']]+=1
    print('')
    print('--'*50)
    for continente, cantidad in paises_por_continente.items():
        # continente toma el valor de la clave y cantidad toma el valor de la cantidad de paises
        print(f'{continente:<10} : {cantidad}')
    print('--'*50)
    print('')
    return


def mostrar_estadisticas():
    while True:
        print('')
        print('ESTADÍSTICAS: ')
        print('')
        print('1) País con mayor y menor población')
        print('2) Promedio de población')
        print('3) Promedio de superficie')
        print('4) Cantidad de paises por continente')
        print('5) Volver atras')
        option=''
        option=input('Ingrese la opción deseada:')
        match option:
            case '1':
                mayor_menor_poblacion()
            case '2':
                promedio_poblacion()
            case '3':
                promedio_superficie()
            case '4':
                cantidad_paises_continente()
            case '5':
                break
            case _:
                print('Opción incorrecta. Intente nuevamente.')

# validaciones
# ------------------------------------------------------------
def tiene_paises():
    """
    Valida si hay paises para mostrar
    Parametros:
    - DATOS_PAISES: lista de diccionarios con datos de paises
    """
    if not DATOS_PAISES:
        print('No hay paises para mostrar.')
        input('Presione enter para continuar: ')
        return False
    return True

# Fin validaciones
# ------------------------------------------------------------

# menu principal
def menu_principal():
    while True:
        print('')
        print('MENU PRINCIPAL: ')
        print('')
        print('1) Agregar pais')
        print('2) Actualizar datos')
        print('3) Buscar pais')
        print('4) Filtrar paises')
        print('5) Ordenar paises')
        print('6) Mostrar estadisticas')
        print('7) Salir')
        opcion=input('Seleccione una opcion: ').strip()
        match opcion:
            case '1':
                agregar_pais()
            case '2':
                actualizar_datos()
            case '3':
                buscar_pais()
            case '4':
                filtrar_pais()
            case '5':
                ordenar_paises()
            case '6':
                mostrar_estadisticas()
            case '7':
                print('Hasta luego!')
                break
            case _:
                print('Opción incorrecta. Intente nuevamente.')

# fin menu principal
# ------------------------------------------------------------

# menu principal
menu_principal()
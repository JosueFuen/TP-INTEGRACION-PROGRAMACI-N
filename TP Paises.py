import csv
import os
nombre_archivo='Country-data.csv'
opcion=''
#Argentina,45376763,2780400,América
if not os.path.exists('Country-data.csv'):
    with open (nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=['nombre','poblacion','superficie','continente'])
        escritor.writeheader()
#Crea una lista de diccionarios con la informacion de los paises
def catalogo_paises():
    paises=[]
    with open (nombre_archivo, newline='', encoding='utf-8' ) as archivo:
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
    for pais in DATOS_PAISES:
        lista.append(pais[f'{territorio}'].lower())
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
    cantidad=input(f"Ingrese {tipo} del país: ").strip()
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
        option=input('Indique a qué continente corresponde el pais elegido: ').strip()
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


#función principal para agregar un nuevo país.
def agregar_pais():
    nombre_pais=validacion_pais()
    poblacion=validacion_digitos('poblacion')
    superficie=validacion_digitos('superficie')
    nombre_continente=validacion_continente()
    nuevo_pais={'nombre':nombre_pais,'poblacion':poblacion,'superficie':superficie,'continente':nombre_continente}

    with open (nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
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
    with open (nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=['nombre','poblacion','superficie','continente'])
        escritor.writeheader()
        escritor.writerows(DATOS_PAISES)


while opcion != '7':
    menu()
    opcion=input('Seleccione una opcion: ').strip()
    match opcion:
        case '1':
            agregar_pais()
        case '2':
            actualizar_datos()
        case '3':
            continue
        case '4':
            continue
        case '5':
            continue
        case '6':
            continue
        case '7':
            print('Hasta luego!')
            break
        case _:
            pausa=input('Opción incorrecta. Intente nuevamente.')
import csv
import os
nombre_archivo='Country-data.csv'
opcion=''

if not os.path.exists('Country-data.csv'):
    with open (nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=['nombre','poblacion','superficie','continente'])
        escritor.writeheader()




def menu():
    print("\n             MENÚ  ")
    print("1)   Agregar país")
    print("2)   Actualizar datos")
    print("3)   Buscar país")
    print("4)   Filtrar países")
    print("5)   Ordenar países")
    print("6)   Mostrar estadísticas")
    print("7)   Salir")


while opcion != '8':
    menu()
    opcion=input('Seleccione una opcion: ').strip()
    match opcion:
        case '1':
            continue
        case '2':
            continue
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
            opcion=input('Opción incorrecta. Intente nuevamente: ')
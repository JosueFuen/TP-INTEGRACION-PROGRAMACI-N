# Gestión de Países

Sistema de gestión de países desarrollado en Python para la materia de Integración de Programación de la UTN.

## Descripción del Programa

Este programa permite gestionar información de países almacenada en un archivo CSV. Ofrece funcionalidades completas para agregar, actualizar, buscar, filtrar, ordenar y generar estadísticas sobre los datos de países. El sistema implementa algoritmos de ordenamiento personalizados y validaciones robustas para garantizar la integridad de los datos.

## Características

- **Gestión de datos**: Agregar y actualizar información de países
- **Búsqueda**: Búsqueda de países por nombre
- **Filtrado**: Filtrar por continente, rango de población o superficie
- **Ordenamiento**: Ordenar países por nombre, población o superficie (ascendente/descendente)
- **Estadísticas**: Generar estadísticas sobre los datos
- **Persistencia**: Datos almacenados en formato CSV

## Estructura de Datos

Cada país contiene los siguientes campos:
- `nombre`: Nombre del país
- `poblacion`: Población total
- `superficie`: Superficie en km
- `continente`: Continente al que pertenece

## Requisitos

- Python 3.x
- Módulos estándar: `csv`, `os`

## Instrucciones de Uso

### Ejecución
Ejecutar el programa:
```bash
python tp_paises.py
```

El programa creará automáticamente el archivo `country_data.csv` si no existe.

### Navegación
- El programa presenta un menú principal con 7 opciones
- Ingrese el número de la opción deseada y presione Enter
- Siga las instrucciones específicas de cada función
- Para volver al menú anterior, seleccione la opción correspondiente

### Validaciones
- Los nombres de países no pueden repetirse
- La población y superficie deben ser números mayores a cero
- Los continentes se seleccionan de una lista predefinida

## Menú Principal

1. **Agregar país**: Ingresar un nuevo país con sus datos
2. **Actualizar datos**: Modificar población y superficie de un país existente
3. **Buscar país**: Buscar países por palabra clave
4. **Filtrar países**: Filtrar por continente o rangos numéricos
5. **Ordenar países**: Ordenar por diferentes criterios
6. **Mostrar estadísticas**: Ver análisis de datos
7. **Salir**: Cerrar el programa

## Algoritmos Implementados

- **Bubble Sort**: Implementación personalizada para ordenamiento de países
- **Búsqueda lineal**: Para filtrado y búsqueda de países
- **Validación de entrada**: Verificación robusta de datos ingresados

## Estructura del Código

- `catalogo_paises()`: Carga datos desde CSV
- `agregar_pais()`: Agrega nuevos países
- `actualizar_datos()`: Actualiza información existente
- `bubble_sort_paises()`: Algoritmo de ordenamiento genérico
- `mostrar_estadisticas()`: Genera análisis estadísticos
- Funciones de validación y filtrado

## Ejemplos de Entradas y Salidas

### Agregar País
```
Ingrese el nombre del país: Argentina
Ingrese la población del país: 45376763
Ingrese la superficie del país: 2780400
Indique el continente: 2
```
**Salida**: País agregado exitosamente

### Buscar País
```
Ingresar nombre de pais: arg
```
**Salida**:
```
[{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}]
```

### Filtrar por Continente
```
Filtrar paises por:
1) Continente
2) Rango de población
3) Rango de superficie
4) Volver atras
Ingrese la opción deseada:1
-----CONTINENTE PARA ELEGIR-----
1) África
2) América
3) Asia
4) Europa
5) Oceanía
Indique el continente: 2
```
**Salida**: Lista de países americanos

### Estadísticas
```
ESTADÍSTICAS:
1) País con mayor y menor población
2) Promedio de población
3) Promedio de superficie
4) Cantidad de paises por continente
5) Volver atras
Ingrese la opción deseada:4
```
**Salida**:
```
----------------------------------------------------------------------------------------------------
América    : 3
Europa     : 2
Asia       : 1
----------------------------------------------------------------------------------------------------
```

## Participación de los Integrantes

**Trabajo Práctico - Integración de Programación**
**Materia: Programación 1**

Este proyecto fue desarrollado como parte del trabajo práctico integrador de la materia Programación 1 de la UTN.

- Josue Fuentes
- Saulo Garcia

## Archivos

- `tp_paises.py`: Código fuente principal
- `country_data.csv`: Base de datos de países (creado automáticamente)
- `README.md`: Documentación del proyecto

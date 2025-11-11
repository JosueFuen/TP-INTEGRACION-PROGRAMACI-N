# Gestión de Países

Sistema de gestión de países desarrollado en Python para la materia de Integración de Programación de la UTN.

## Descripción

Este programa permite gestionar información de países almacenada en un archivo CSV. Ofrece funcionalidades completas para agregar, actualizar, buscar, filtrar, ordenar y generar estadísticas sobre los datos de países.

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

## Uso

Ejecutar el programa:
```bash
python tp_paises.py
```

El programa creará automáticamente el archivo `country_data.csv` si no existe.

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

## Archivos

- `tp_paises.py`: Código fuente principal
- `country_data.csv`: Base de datos de países (creado automáticamente)
- `README.md`: Documentación del proyecto

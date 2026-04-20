#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:49:18 2026

@author: giuliamaniotti
"""

from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (calcular_promedio_senal, calcular_minimo_senal, 
calcular_maximo_senal, calcular_fc_desde_datos)
from src.validacion_datos import validar_registro


def main():
    """
    Qué hace la función:
    Coordina el flujo principal del programa.

    Carga los datos del archivo, valida los registros, solicita el ID de un
    participante, filtra sus datos, calcula métricas de la señal ECG
    y muestra los resultados en pantalla.

    Parámetros:
    - No recibe parámetros.

    Retorna:
    - No retorna valores.
    """
    
    try:
        datos = cargar_datos("datos/PulseLab_mock_data.csv") 
    except Exception as e:
        print("Error en carga de datos:", e)


    if len(datos) == 0:
        print("No se pudieron cargar datos válidos.")
        return

    datos_validos = []

    for registro in datos:
        if validar_registro(registro):
            datos_validos.append(registro)

    if len(datos_validos) == 0:
        print("No hay registros válidos para procesar.")
        return

    while True:
        try:
            id_participante = int(input("Ingrese el ID del participante: "))
            if id_participante < 0:
                print("Error: el ID no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: debe ingresar un número entero válido.")

    participante = filtrar_por_participante(datos_validos, id_participante)

    if participante is None:
        print("No se encontró el participante.")
        return

    promedio = calcular_promedio_senal(participante)
    minimo = calcular_minimo_senal(participante)
    maximo = calcular_maximo_senal(participante)
    frecuencia = calcular_fc_desde_datos(participante)

    print("\n--- RESULTADOS ---")
    print("ID participante:", id_participante)
    print("Promedio señal ECG:", promedio)
    print("Mínimo ECG:", minimo)
    print("Máximo ECG:", maximo)
    print("Frecuencia cardíaca:", frecuencia, "BPM")


main()

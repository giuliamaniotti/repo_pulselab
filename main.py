#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:49:18 2026

@author: giuliamaniotti
"""

from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import (
    calcular_promedio_senal,
    calcular_minimo_senal,
    calcular_maximo_senal,
    calcular_fc_desde_datos
)


def main():
    """
    Qué hace la función:
    Coordina el flujo principal del programa.

    Carga los datos del archivo, solicita el ID de un participante,
    busca sus datos, calcula las métricas de la señal ECG
    y muestra los resultados en pantalla.

    Parámetros:
    - No recibe parámetros.

    Retorna:
    - No retorna valores.

    Manejo de errores:
    - Si ocurre un error durante la carga, búsqueda o cálculo,
      muestra un mensaje de error crítico en consola y finaliza
      la ejecución.
    """

    try:
        ruta = "datos/PulseLab_mock_data_error01.csv"
        datos = cargar_datos(ruta)
    except Exception as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: cargar_datos")
        return

    try:
        id_participante = int(input("Ingrese el ID del participante: "))

        if id_participante <= 0:
            raise ValueError("El ID del participante debe ser un entero positivo.")
    except ValueError as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: main")
        return

    try:
        participante = filtrar_por_participante(datos, id_participante)
    except Exception as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: filtrar_por_participante")
        return

    try:
        promedio = calcular_promedio_senal(participante)
        minimo = calcular_minimo_senal(participante)
        maximo = calcular_maximo_senal(participante)
        frecuencia = calcular_fc_desde_datos(participante)
    except Exception as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: metricas")
        return

    print("\n--- RESULTADOS ---")
    print(f"ID participante: {id_participante}")
    print(f"Promedio señal ECG: {promedio}")
    print(f"Mínimo ECG: {minimo}")
    print(f"Máximo ECG: {maximo}")
    print(f"Frecuencia cardíaca: {frecuencia} BPM")


main()

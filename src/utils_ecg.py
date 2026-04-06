#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:17:09 2026

@author: giuliamaniotti
"""

def detectar_picos_qrs(tiempos: list, senal: list, umbral: float = 0.9, distancia_minima: float =
0.3) -> list:
    
    """
    Detecta picos en la señal ECG.
    
    Parámetros:
    - tiempos: lista de tiempos
    - senal: lista de valores de la señal
    - umbral: valor mínimo para considerar un pico
    - distancia_minima: tiempo mínimo entre picos

    Retorna:
    - lista de tiempos donde ocurren los picos
    """
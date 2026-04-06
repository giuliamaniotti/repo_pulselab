#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:42 2026

@author: giuliamaniotti
"""

def filtrar_por_participante(datos: list, id_participante: int) -> dict:
    """
    Qué hace la función:
    Selecciona y devuelve los datos correspondientes a un participante.

    Parámetros:
    - datos: lista de diccionarios con los registros de participantes
    - id_participante: identificador del participante a buscar

    Retorna:
    - dict: datos del participante encontrado
    - None: si no se encuentra el participante
    """
    for participante in datos:
        if participante["id_participante"] == id_participante:
            return participante

    return None

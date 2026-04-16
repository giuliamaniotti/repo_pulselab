#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:42 2026

@author: giuliamaniotti
"""

def filtrar_por_participante(datos: list, id_participante: int) -> dict:
    """
    Qué hace la función:
    Busca y devuelve los datos de un participante según su ID.

    Parámetros:
    - datos: list. Lista de diccionarios con los registros.
    - id_participante: int. ID del participante a buscar.

    Retorna:
    - dict: registro del participante encontrado.
    - None: si no se encuentra.
    """
    if not isinstance(datos, list):
        return None

    if not isinstance(id_participante, int):
        return None

    for registro in datos:
        if isinstance(registro, dict) and registro.get("id_participante") == id_participante:
            return registro

    return None


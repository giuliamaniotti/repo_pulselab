#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:42 2026

@author: giuliamaniotti
"""

def filtrar_por_participante(datos: list, id_participante: int) -> dict:

    """
    Qué hace la función:
    Busca dentro de la base de datos cargada el registro correspondiente
    a un participante específico, identificado por su ID.

    Parámetros:
    - datos: list. Lista de diccionarios con los datos ya cargados y agrupados
      por participante.
    - id_participante: int. Identificador del participante que se desea buscar.

    Retorna:
    - dict: diccionario con los datos del participante encontrado.

    Lanza:
    - TypeError: si la base de datos no es una lista.
    - ValueError: si la base de datos está vacía.
    - TypeError: si el ID recibido no es un entero.
    - ValueError: si el participante no existe en la base de datos.
    """
    
    if not isinstance(datos, list):
        raise TypeError("La base de datos debe ser una lista.")

    if len(datos) == 0:
        raise ValueError("La base de datos está vacía.")

    if not isinstance(id_participante, int):
        raise TypeError("El ID del participante debe ser un entero.")

    for registro in datos:
        if registro.get("id_participante") == id_participante:
            return registro

    raise ValueError(f"El participante {id_participante} no existe.")


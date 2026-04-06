#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:41 2026

@author: giuliamaniotti
"""

def verificar_tipo_datos(registro: dict) -> bool:
    
    """
    
    Verifica que el registro tenga todas las claves esperadas y que
    cada una sea del tipo de dato correcto.

    Parámetros:
    - registro: diccionario con los datos de un participante.

    Retorna:
    - True si el registro tiene la estructura y tipos correctos.
    - False en caso contrario.
    
    """
    
    claves_esperadas = [
        "id_participante",
        "tiempo",
        "valor",
        "fase",
        "condicion_experimental",
        "hit"
        ]

    for clave in claves_esperadas:
        if clave not in registro:
            return False
    
    if type(registro["id_participante"]) != int or \
      type(registro["tiempo"]) != list or \
      type(registro["valor"]) != list or \
      type(registro["fase"]) != list or \
      type(registro["condicion_experimental"]) != list or \
      type(registro["hit"]) != list:
       return False        
   
    if len(registro["tiempo"]) != len(registro["valor"]) or \
      len(registro["tiempo"]) != len(registro["fase"]) or \
      len(registro["tiempo"]) != len(registro["condicion_experimental"]) or \
      len(registro["tiempo"]) != len(registro["hit"]):
          return False

    for tiempo in registro["tiempo"]:
        if type(tiempo) != int and type(tiempo) != float:
            return False

    for valor in registro["valor"]:
        if type(valor) != int and type(valor) != float:
            return False

    for fase in registro["fase"]:
        if type(fase) != str:
            return False

    for condicion in registro["condicion_experimental"]:
        if type(condicion) != str:
            return False

    for hit in registro["hit"]:
        if type(hit) != int and type(hit) != bool:
            return False

    return True



def verificar_valores_validos(registro: dict) -> bool:
    
    """
    
    Verifica que los valores del registro estén dentro de los dominios
    válidos del proyecto PulseLab.

    Parámetros:
    - registro: diccionario con los datos de un participante.

    Retorna:
    - True si los valores son válidos.
    - False si algún valor no cumple con lo esperado.
  
    """
    
    fases_validas = ["baseline", "tarea"]
    condiciones_validas = ["competencia", "cooperacion"]
    hits_validos = [0, 1, True, False]

    if registro["id_participante"] < 0:
        return False

    for tiempo in registro["tiempo"]:
        if tiempo < 0:
            return False

    for fase in registro["fase"]:
        if fase not in fases_validas:
            return False

    for condicion in registro["condicion_experimental"]:
        if condicion not in condiciones_validas:
            return False

    for hit in registro["hit"]:
        if hit not in hits_validos:
            return False

    return True


def validar_registro(registro: dict) -> bool:
    
    """
    
    Valida un registro completo de PulseLab verificando primero
    los tipos de datos y luego los valores permitidos.

    Parámetros:
    - registro: diccionario con los datos de un participante.

    Retorna:
    - True si el registro es válido.
    - False si no supera alguna validación.
    """
    
    if not verificar_tipo_datos(registro):
        return False

    if not verificar_valores_validos(registro):
        return False

    return True
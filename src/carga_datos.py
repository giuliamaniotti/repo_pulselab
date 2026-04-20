#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:37 2026

@author: giuliamaniotti
"""

def parsear_linea(linea: str) -> list:
    """
    Qué hace la función:
   Procesa una línea del archivo de datos, separando sus componentes
   y convirtiéndolos a los tipos correctos.

   Parámetros:
   - linea: str. Línea del archivo CSV.

   Retorna:
   - list: [id_participante, tiempo, valor, fase, condicion_experimental, hit]

   Lanza:
   - ValueError: si la línea no tiene 6 campos o si algún dato no puede convertirse.
    """
    partes = linea.strip().split(",")

    if len(partes) != 6:
        raise ValueError("La línea no tiene exactamente 6 campos.")

    try:
        id_participante = int(partes[0].strip())
        tiempo = float(partes[1].strip())
        valor = float(partes[2].strip())
        fase = partes[3].strip()
        condicion_experimental = partes[4].strip()
        hit_str = partes[5].strip().lower()
        if hit_str == "true":
            hit = True
        elif hit_str == "false":
            hit = False 
        else:
            raise ValueError(f"Valor inválido para hit: {partes[5].strip()}")
    except ValueError as error:
        raise ValueError(f"Error de conversión en la línea: {linea.strip()}") from error

    return [id_participante, tiempo, valor, fase, condicion_experimental, hit]



def cargar_datos(ruta) -> list:
    
    """
    Qué hace la función:
    Lee el archivo de datos, parsea cada línea y agrupa los registros por participante.

    Parámetros:
    - ruta: str. Ruta al archivo CSV.

    Retorna:
    - list: lista de diccionarios, uno por participante.

    Manejo de errores:
    - Si el archivo no existe, devuelve lista vacía.
    - Si una línea tiene error, la ignora y sigue con la siguiente.
    """
    participantes = {}

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            for numero_linea, linea in enumerate(archivo, start=1):
                if linea.strip() == "":
                    continue

                try:
                    id_participante, tiempo, valor, fase, condicion_experimental, hit = parsear_linea(linea)
                except ValueError:
                    print(f"Línea {numero_linea} ignorada por formato inválido.")
                    continue

                if id_participante not in participantes:
                    participantes[id_participante] = {
                        "id_participante": id_participante,
                        "tiempo": [],
                        "valor": [],
                        "fase": [],
                        "condicion_experimental": [],
                        "hit": []
                    }

                participantes[id_participante]["tiempo"].append(tiempo)
                participantes[id_participante]["valor"].append(valor)
                participantes[id_participante]["fase"].append(fase)
                participantes[id_participante]["condicion_experimental"].append(condicion_experimental)
                participantes[id_participante]["hit"].append(hit)

    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
        return []
    except OSError:
        print(f"Error: no se pudo abrir el archivo '{ruta}'.")
        return []

    return list(participantes.values())
    
        



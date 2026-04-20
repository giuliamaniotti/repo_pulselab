#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:46:37 2026

@author: giuliamaniotti
"""

def parsear_linea(linea: str, numero_linea: int) -> list:
    
    """
    Qué hace la función:
    Procesa una línea del archivo CSV de PulseLab, separa sus columnas,
    valida que la estructura sea correcta, convierte los datos a los tipos
    esperados y controla que los valores cumplan las reglas del proyecto.

    Parámetros:
    - linea: str. Línea leída del archivo CSV.
    - numero_linea: int. Número de línea dentro del archivo, usado para
      informar errores con mayor precisión.

    Retorna:
    - list: lista con los datos ya validados y convertidos en este orden:
      [id_participante, tiempo, valor, fase, condicion_experimental, hit]

    Lanza:
    - TypeError: si la línea recibida no es un string.
    - ValueError: si la línea está vacía.
    - ValueError: si la línea no tiene exactamente 6 columnas.
    - ValueError: si algún campo obligatorio está vacío.
    - ValueError: si el ID no puede convertirse a entero o no es positivo.
    - ValueError: si el tiempo no puede convertirse a float o es negativo.
    - ValueError: si el valor de la señal ECG no puede convertirse a float
      o está fuera del rango permitido.
    - ValueError: si la fase no pertenece a las categorías válidas.
    - ValueError: si la condición experimental no pertenece a las categorías válidas.
    - ValueError: si el campo hit no tiene el formato booleano permitido
      ('True' o 'False').
    """
    
    if not isinstance(linea, str):
        raise TypeError("La línea debe ser un string.")

    if linea.strip() == "":
        raise ValueError(f"Línea {numero_linea} vacía.")

    partes = linea.strip().split(",")

    if len(partes) != 6:
        raise ValueError(f"Línea {numero_linea}: se esperaban 6 columnas y se encontraron {len(partes)}.")

    for i, campo in enumerate(partes):
        if campo.strip() == "":
            raise ValueError(f"Línea {numero_linea}: campo vacío en columna {i+1}.")

    try:
        id_participante = int(partes[0].strip())
    except ValueError:
        raise ValueError(f"Línea {numero_linea}: ID inválido.")

    if id_participante <= 0:
        raise ValueError(f"Línea {numero_linea}: el ID debe ser entero positivo.")

    try:
        tiempo = float(partes[1].strip())
    except ValueError:
        raise ValueError(f"Línea {numero_linea}: tiempo inválido.")

    if tiempo < 0:
        raise ValueError(f"Línea {numero_linea}: el tiempo no puede ser negativo.")

    try:
        valor = float(partes[2].strip())
    except ValueError:
        raise ValueError(f"Línea {numero_linea}: valor ECG inválido.")

    VALOR_MIN = -5.0
    VALOR_MAX = 5.0
    if valor < VALOR_MIN or valor > VALOR_MAX:
        raise ValueError(
            f"Línea {numero_linea}: valor ECG fuera de rango ({valor})."
        )

    fase = partes[3].strip()
    if fase not in ["baseline", "tarea"]:
        raise ValueError(f"Línea {numero_linea}: fase inválida '{fase}'.")

    condicion_experimental = partes[4].strip()
    if condicion_experimental not in ["competencia", "cooperacion"]:
        raise ValueError(f"Línea {numero_linea}: condición inválida '{condicion_experimental}'.")

    hit_str = partes[5].strip()
    if hit_str == "True":
        hit = True
    elif hit_str == "False":
        hit = False
    else:
        raise ValueError(f"Línea {numero_linea}: hit inválido '{hit_str}'. Debe ser True o False.")

    return [id_participante, tiempo, valor, fase, condicion_experimental, hit]



def cargar_datos(ruta: str) -> list:

    """
    Qué hace la función:
    Abre el archivo CSV indicado por la ruta, verifica que pueda leerse,
    controla que no esté vacío, procesa cada línea con la función
    parsear_linea() y agrupa los datos por participante en una estructura
    de diccionarios.

    Además, valida que la variable tiempo esté ordenada de forma creciente
    para cada participante antes de guardar los datos.

    Parámetros:
    - ruta: str. Ruta relativa o absoluta del archivo CSV a cargar.

    Retorna:
    - list: lista de diccionarios, donde cada diccionario contiene los datos
      agrupados de un participante.

    Lanza:
    - ValueError: si la ruta recibida no es válida.
    - FileNotFoundError: si el archivo no existe en la ruta indicada.
    - OSError: si el archivo existe pero no puede abrirse.
    - ValueError: si el archivo está vacío.
    - ValueError: si alguna línea del archivo contiene un dato inválido.
    - ValueError: si el tiempo no está ordenado de forma creciente dentro
      de un mismo participante.
    - ValueError: si luego de la carga no quedó ningún participante válido.
    """
    
    if not isinstance(ruta, str) or ruta.strip() == "":
        raise ValueError("La ruta del archivo es inválida.")

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo '{ruta}'.")
    except OSError:
        raise OSError(f"No se pudo abrir el archivo '{ruta}'.")

    if len(lineas) == 0:
        raise ValueError("El archivo está vacío.")

    participantes = {}

    for numero_linea, linea in enumerate(lineas, start=1):
        id_participante, tiempo, valor, fase, condicion_experimental, hit = parsear_linea(linea, numero_linea)

        if id_participante not in participantes:
            participantes[id_participante] = {
                "id_participante": id_participante,
                "tiempo": [],
                "valor": [],
                "fase": [],
                "condicion_experimental": [],
                "hit": []
            }

        if len(participantes[id_participante]["tiempo"]) > 0:
            ultimo_tiempo = participantes[id_participante]["tiempo"][-1]
            if tiempo <= ultimo_tiempo:
                raise ValueError(
                    f"Línea {numero_linea}: tiempo no creciente para participante {id_participante}."
                )

        participantes[id_participante]["tiempo"].append(tiempo)
        participantes[id_participante]["valor"].append(valor)
        participantes[id_participante]["fase"].append(fase)
        participantes[id_participante]["condicion_experimental"].append(condicion_experimental)
        participantes[id_participante]["hit"].append(hit)

    if len(participantes) == 0:
        raise ValueError("La base de datos quedó vacía después de la carga.")

    return list(participantes.values())
    
        



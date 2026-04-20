from src.detectar_picos import detectar_picos_qrs


def calcular_promedio_senal(datos: dict) -> float:
    """
    Qué hace la función:
    Calcula el promedio de los valores de la señal ECG.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float. Promedio de la señal.
    """
    if not isinstance(datos, dict):
        return 0

    senal = datos.get("valor", [])

    if not isinstance(senal, list) or len(senal) == 0:
        return 0

    return sum(senal) / len(senal)


def calcular_minimo_senal(datos: dict) -> float:
    """
    Qué hace la función:
    Calcula el valor mínimo de la señal ECG.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float. Valor mínimo de la señal.
    """
    if not isinstance(datos, dict):
        return 0

    senal = datos.get("valor", [])

    if not isinstance(senal, list) or len(senal) == 0:
        return 0

    return min(senal)


def calcular_maximo_senal(datos: dict) -> float:
    """
    Qué hace la función:
    Calcula el valor máximo de la señal ECG.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float. Valor máximo de la señal.
    """
    if not isinstance(datos, dict):
        return 0

    senal = datos.get("valor", [])

    if not isinstance(senal, list) or len(senal) == 0:
        return 0

    return max(senal)


def calcular_frecuencia_cardiaca(picos: list) -> float:
    """
    Qué hace la función:
    Calcula la frecuencia cardíaca en BPM a partir de los picos detectados.

    Parámetros:
    - picos: list. Lista de tiempos donde se detectaron picos.

    Retorna:
    - float. Frecuencia cardíaca en latidos por minuto.
    """
    if not isinstance(picos, list):
        return 0

    if len(picos) < 2:
        return 0

    tiempo_total = picos[-1] - picos[0]

    if tiempo_total <= 0:
        return 0

    cantidad_intervalos = len(picos) - 1
    frecuencia = (cantidad_intervalos / tiempo_total) * 60

    return frecuencia


def calcular_fc_desde_datos(datos: dict) -> float:
    """
    Qué hace la función:
    Detecta los picos de la señal y calcula la frecuencia cardíaca.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float. Frecuencia cardíaca en BPM.
    """
    if not isinstance(datos, dict):
        return 0

    tiempos = datos.get("tiempo", [])
    senal = datos.get("valor", [])

    if not isinstance(tiempos, list) or not isinstance(senal, list):
        return 0

    picos = detectar_picos_qrs(tiempos, senal)
    return calcular_frecuencia_cardiaca(picos)





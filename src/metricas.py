from src.detectar_picos import detectar_picos_qrs


def validar_datos_metricas(datos: dict) -> None:
    
    """
    Qué hace la función:
    Verifica que los datos de un participante tengan la estructura mínima
    necesaria para poder calcular métricas básicas sobre la señal ECG.

    Parámetros:
    - datos: dict. Diccionario con los datos de un participante.

    Retorna:
    - None. La función no devuelve ningún valor; solo valida.
      Si encuentra un problema, lanza una excepción.

    Lanza:
    - TypeError: si los datos no se reciben en un diccionario.
    - ValueError: si faltan campos necesarios para calcular métricas.
    - ValueError: si las listas de tiempo o valor están vacías.
    - ValueError: si las listas de tiempo y valor tienen distinta longitud.
    """
    
    if not isinstance(datos, dict):
        raise TypeError("Los datos deben ser un diccionario.")

    if "tiempo" not in datos or "valor" not in datos:
        raise ValueError("Faltan campos necesarios para calcular métricas.")

    tiempos = datos["tiempo"]
    valores = datos["valor"]

    if not isinstance(tiempos, list) or not isinstance(valores, list):
        raise TypeError("Los campos 'tiempo' y 'valor' deben ser listas.")

    if len(tiempos) == 0 or len(valores) == 0:
        raise ValueError("No hay datos suficientes para calcular métricas.")

    if len(tiempos) != len(valores):
        raise ValueError("Las listas 'tiempo' y 'valor' deben tener el mismo largo.")


def calcular_promedio_senal(datos: dict) -> float:
    
    """
    Qué hace la función:
    Calcula el promedio aritmético de los valores de la señal ECG.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float: promedio de la señal ECG.

    Lanza:
    - TypeError: si los datos no tienen el formato esperado.
    - ValueError: si no hay datos suficientes para calcular el promedio.
    """
    
    validar_datos_metricas(datos)
    return sum(datos["valor"]) / len(datos["valor"])


def calcular_minimo_senal(datos: dict) -> float:
    
    """
    Qué hace la función:
    Calcula el valor mínimo de la señal ECG.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float: valor mínimo de la señal ECG.

    Lanza:
    - TypeError: si los datos no tienen el formato esperado.
    - ValueError: si no hay datos suficientes para calcular el mínimo.
    """
    
    validar_datos_metricas(datos)
    return min(datos["valor"])


def calcular_maximo_senal(datos: dict) -> float:
    
    """
    Qué hace la función:
    Calcula el valor máximo de la señal ECG.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float: valor máximo de la señal ECG.

    Lanza:
    - TypeError: si los datos no tienen el formato esperado.
    - ValueError: si no hay datos suficientes para calcular el máximo.
    """
    
    validar_datos_metricas(datos)
    return max(datos["valor"])


def calcular_frecuencia_cardiaca(picos: list) -> float:
    
    """
    Qué hace la función:
    Calcula la frecuencia cardíaca en BPM a partir de los tiempos
    en los que se detectaron picos QRS.

    Parámetros:
    - picos: list. Lista de tiempos donde se detectaron picos.

    Retorna:
    - float: frecuencia cardíaca en latidos por minuto.

    Lanza:
    - TypeError: si picos no es una lista.
    - ValueError: si hay menos de dos picos.
    - ValueError: si el tiempo total entre el primer y el último pico no es válido.
    """
    
    if not isinstance(picos, list):
        raise TypeError("Los picos deben recibirse en una lista.")

    if len(picos) < 2:
        raise ValueError("No hay picos suficientes para calcular la frecuencia cardíaca.")

    tiempo_total = picos[-1] - picos[0]

    if tiempo_total <= 0:
        raise ValueError("El intervalo de tiempo entre picos no es válido.")

    cantidad_intervalos = len(picos) - 1
    frecuencia = (cantidad_intervalos / tiempo_total) * 60

    return frecuencia


def calcular_fc_desde_datos(datos: dict) -> float:
    
    """
    Qué hace la función:
    Detecta los picos QRS de la señal ECG y calcula la frecuencia cardíaca
    del participante en latidos por minuto.

    Parámetros:
    - datos: dict. Datos del participante.

    Retorna:
    - float: frecuencia cardíaca en BPM.

    Lanza:
    - TypeError: si los datos no tienen el formato esperado.
    - ValueError: si no hay datos suficientes para detectar picos.
    - ValueError: si no se detectan picos suficientes para calcular
      la frecuencia cardíaca.
    """
    
    validar_datos_metricas(datos)

    tiempos = datos["tiempo"]
    senal = datos["valor"]

    if len(tiempos) < 3:
        raise ValueError("No hay datos suficientes para detectar picos.")

    picos = detectar_picos_qrs(tiempos, senal)

    if len(picos) < 2:
        raise ValueError("No hay picos suficientes para calcular la frecuencia cardíaca.")

    return calcular_frecuencia_cardiaca(picos)



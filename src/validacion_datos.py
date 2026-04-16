
def verificar_tipo_datos(registro):
    """
    Verifica que un registro tenga la estructura correcta y que los tipos de datos sean válidos.

    La función controla que:
    - El registro contenga todas las claves esperadas.
    - El identificador del participante sea un número entero.
    - Todas las listas del registro tengan la misma longitud.
    - Los datos dentro de cada lista sean del tipo correspondiente:
        * tiempo: números (int o float)
        * valor: números (int o float)
        * fase: texto (str)
        * condicion_experimental: texto (str)
        * hit: números enteros (int)

    Parámetros:
    - registro (dict): diccionario con los datos de un participante.

    Retorna:
    - bool: True si el registro cumple con la estructura y tipos correctos.
            False en caso contrario.
    """

    claves = ["id_participante", "tiempo", "valor", "fase", "condicion_experimental", "hit"]

    for clave in claves:
        if clave not in registro:
            return False

    if type(registro["id_participante"]) != int:
        return False

    cantidad = len(registro["tiempo"])

    if len(registro["valor"]) != cantidad:
        return False
    if len(registro["fase"]) != cantidad:
        return False
    if len(registro["condicion_experimental"]) != cantidad:
        return False
    if len(registro["hit"]) != cantidad:
        return False

    for tiempo in registro["tiempo"]:
        if type(tiempo) != float and type(tiempo) != int:
            return False

    for valor in registro["valor"]:
        if type(valor) != float and type(valor) != int:
            return False

    for fase in registro["fase"]:
        if type(fase) != str:
            return False

    for condicion in registro["condicion_experimental"]:
        if type(condicion) != str:
            return False

    for hit in registro["hit"]:
        if type(hit) != int:
            return False

    return True




def verificar_valores_validos(registro: dict) -> bool:
    """
    Qué hace la función:
    Verifica que los valores del registro estén dentro de rangos o conjuntos válidos.

    Parámetros:
    - registro: dict. Diccionario con los datos de un participante.

    Retorna:
    - bool: True si los valores son válidos, False en caso contrario.
    """
    if registro["id_participante"] < 0:
        return False

    for tiempo in registro["tiempo"]:
        if tiempo < 0:
            return False

    fases_validas = {"baseline", "estimulo", "recuperacion"}
    for fase in registro["fase"]:
        if fase.strip().lower() not in fases_validas:
            return False

    condiciones_validas = {"control", "experimental"}
    for condicion in registro["condicion_experimental"]:
        if condicion.strip().lower() not in condiciones_validas:
            return False

    for hit in registro["hit"]:
        if hit not in [0, 1]:
            return False

    return True


def validar_registro(registro: dict) -> bool:
    """
    Qué hace la función:
    Integra la validación de tipos y de valores.

    Parámetros:
    - registro: dict. Datos de un participante.

    Retorna:
    - bool: True si el registro es válido, False en caso contrario.
    """
    if not verificar_tipo_datos(registro):
        return False

    if not verificar_valores_validos(registro):
        return False

    return True

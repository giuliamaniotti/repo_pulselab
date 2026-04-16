# repo_pulselab

Integrantes: Juana Muruzeta,Regina Francucci, 
Giulia Maniotti y Delfina Fernandez Covaro

Todos los integrantes del grupo fueron agregados como colaboradores al repositorio, junto con el docente correspondiente.

## Descripción del proyecto

Este proyecto tiene como objetivo procesar datos de señales cardíacas (ECG) obtenidos de distintos participantes.

El programa permite:
- cargar los datos desde un archivo CSV,
- organizar la información por participante,
- validar que los datos sean correctos,
- calcular métricas de la señal,
- y mostrar los resultados.

Las métricas que se calculan son:
- promedio de la señal,
- valor mínimo,
- valor máximo,
- frecuencia cardíaca (a partir de detección de picos).

El programa está dividido en módulos, donde cada archivo cumple una función específica.


---

El objetivo principal es construir un sistema modular y organizado que 
permita analizar señales fisiológicas y extraer información relevante 
sobre la actividad cardíaca en diferentes condiciones experimentales.

---

## Estructura del repositorio

- `main.py`: programa principal
- `src/carga_datos.py`: carga y parseo de datos
- `src/validacion_datos.py`: validaciones de estructura y valores
- `src/procesamiento_datos.py`: filtrado por participante
- `src/metricas.py`: cálculo de métricas
- `src/utils_ecg.py`: detección de picos ECG
- `diagramas/`: diagramas de flujo del programa

---

## Errores y Validaciones

### `parsear_linea(linea)`
- Error si la línea no tiene la cantidad correcta de datos.
- Error si no se pueden convertir los valores a números.
- Se usa `try/except` para evitar que el programa se rompa.

---

### `cargar_datos(ruta)`
- Error si el archivo no existe.
- Error si una línea está mal formada.
- Se usa `try/except` para abrir el archivo y para procesar cada línea.
- Las líneas con error se ignoran.

---

### `verificar_tipo_datos(registro)`
- Verifica que estén todas las claves necesarias.
- Controla que los tipos de datos sean correctos.
- Verifica que todas las listas tengan la misma longitud.
- Si algo está mal, devuelve `False`.

---

### `verificar_valores_validos(registro)`
- Controla que los valores estén dentro de rangos válidos.
- Ejemplo:
  - tiempos no negativos
  - valores de `hit` sean 0 o 1
- Si encuentra un error, devuelve `False`.

---

### `validar_registro(registro)`
- Combina las dos validaciones anteriores.
- Solo devuelve `True` si todo está correcto.

---

### `filtrar_por_participante(datos, id_participante)`
- Si el participante no existe, devuelve `None`.
- Se controla esto en el programa principal.

---

### `calcular_promedio_senal(datos)`
- Si la señal está vacía, devuelve `0`.
- Evita errores de división.

---

### `calcular_minimo_senal(datos)`
- Si no hay datos, devuelve `0`.

---

### `calcular_maximo_senal(datos)`
- Si no hay datos, devuelve `0`.

---

### `detectar_picos_qrs(tiempos, senal)`
- Si las listas están vacías o tienen distinto tamaño, devuelve lista vacía.
- Si no detecta picos, devuelve lista vacía.

---

### `calcular_frecuencia_cardiaca(picos)`
- Si hay menos de dos picos, devuelve `0`.
- Evita dividir por cero.

---

### `calcular_fc_desde_datos(datos)`
- Usa las funciones anteriores.
- Si no se pueden calcular los picos, devuelve `0`.

---

### `main()`
- Usa `try/except` para validar el input del usuario.
- Si el usuario ingresa algo incorrecto, se vuelve a pedir.
- Si el participante no existe, se muestra un mensaje.
- Si no hay datos válidos, el programa termina sin romperse.

---

## Observaciones

El programa está pensado para manejar errores sin interrumpirse, usando:
- `try/except` cuando puede fallar algo externo (archivo o input),
- validaciones con `if` en el resto de las funciones.

Además, cada función cumple una tarea específica, lo que hace el código más claro y fácil de mantener.



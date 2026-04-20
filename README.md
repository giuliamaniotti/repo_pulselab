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

El sistema está diseñado para detectar errores en los datos y detener la ejecución de forma controlada, informando el problema.

---

### `parsear_linea(linea, numero_linea)`
- Error si la línea está vacía.
- Error si no tiene exactamente 6 columnas.
- Error si hay campos vacíos.
- Error si los datos no pueden convertirse a los tipos correctos.
- Error si el ID no es entero positivo.
- Error si el tiempo es negativo.
- Error si el valor ECG está fuera de rango.
- Error si la fase o condición no son válidas.
- Error si `hit` no es "True" o "False".

---

### `cargar_datos(ruta)`
- Error si la ruta es inválida.
- Error si el archivo no existe o no puede abrirse.
- Error si el archivo está vacío.
- Error si alguna línea contiene datos inválidos.
- Error si el tiempo no es creciente para un participante.
- Error si la base de datos queda vacía luego de la carga.

---

### `filtrar_por_participante(datos, id_participante)`
- Error si los datos no son una lista.
- Error si la base de datos está vacía.
- Error si el ID no es entero.
- Error si el participante no existe.

---

### `calcular_promedio_senal(datos)`
- Error si los datos no tienen formato válido.
- Error si no hay datos suficientes para calcular.

---

### `calcular_minimo_senal(datos)`
- Error si los datos no tienen formato válido.
- Error si no hay datos suficientes para calcular.

---

### `calcular_maximo_senal(datos)`
- Error si los datos no tienen formato válido.
- Error si no hay datos suficientes para calcular.

---

### `detectar_picos_qrs(tiempos, senal)`
- Error si las listas no tienen el formato correcto.
- Error si no hay datos suficientes para detectar picos.

---

### `calcular_frecuencia_cardiaca(picos)`
- Error si los picos no tienen formato válido.
- Error si hay menos de dos picos.
- Error si el intervalo de tiempo no es válido.

---

### `calcular_fc_desde_datos(datos)`
- Error si los datos no tienen formato válido.
- Error si no hay datos suficientes para detectar picos.
- Error si no se detectan suficientes picos.

---

### `main()`
- Maneja los errores con `try/except`.
- Muestra errores con formato:

---

## Modelado del sistema usando Objetos

Aunque en esta entrega no implementamos Programación Orientada a Objetos, el sistema puede modelarse utilizando clases para organizar mejor sus responsabilidades.

---

### Clase `RegistroECG`

Representa una línea del archivo CSV.

**Atributos:**
- id_participante: int  
- tiempo: float  
- valor: float  
- fase: str  
- condicion_experimental: str  
- hit: bool  

**Métodos:**
- validar_tipos()  
- validar_valores()  
- to_dict()  

---

### Clase `Participante`

Representa a un participante con todos sus datos agrupados.

**Atributos:**
- id_participante: int  
- tiempos: list  
- valores: list  
- fases: list  
- condiciones_experimentales: list  
- hits: list  

**Métodos:**
- agregar_registro(registro)  
- validar_tiempo_creciente()  
- calcular_promedio_senal()  
- calcular_minimo_senal()  
- calcular_maximo_senal()  
- calcular_frecuencia_cardiaca()  

---

### Clase `CargadorCSV`

Se encarga de leer y validar el archivo.

**Atributos:**
- ruta: str  
- lineas: list  

**Métodos:**
- abrir_archivo()  
- parsear_linea()  
- cargar_datos()  

---

### Clase `AnalizadorECG`

Se encarga del cálculo de métricas.

**Atributos:**
- participante: Participante  

**Métodos:**
- validar_datos_metricas()  
- calcular_promedio_senal()  
- calcular_minimo_senal()  
- calcular_maximo_senal()  
- calcular_frecuencia_cardiaca()  

---

### Clase `DetectorPicosQRS`

Encapsula el algoritmo de detección de picos.

**Atributos:**
- tiempos: list  
- senal: list  

**Métodos:**
- detectar_picos()  
- validar_senal()  

---

### Clase `SistemaPulseLab`

Coordina todo el flujo del programa.

**Atributos:**
- ruta_archivo: str  
- participantes: list  

**Métodos:**
- iniciar()  
- cargar_participantes()  
- buscar_participante(id)  
- mostrar_resultados()  
- manejar_errores()  

---

## Observaciones

El programa está diseñado para:
- detectar errores en la entrada de datos,
- detener la ejecución de forma controlada,
- y comunicar claramente el problema.

Además, cada módulo cumple una función específica, lo que hace al sistema más claro, modular y fácil de mantener.
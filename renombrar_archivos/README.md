
# Proyecto: Renombrador Automático de Archivos de Texto usando IA

Este proyecto es un script en Python que utiliza procesamiento de lenguaje natural (NLP) para analizar archivos de texto dentro de una carpeta y renombrarlos de manera automática según el tema principal identificado. Esto es útil para organizar tus archivos de manera eficiente, asignándoles nombres descriptivos basados en el contenido de cada archivo.

## Características
- Utiliza un clasificador de IA para analizar el contenido de archivos de texto.
- Clasifica el contenido en temas predefinidos.
- Renombra automáticamente los archivos con un prefijo descriptivo del tema principal.

## Requisitos

- Python 3.7+
- Bibliotecas de Python:
  - `transformers`
  - `torch`

## Instalación

1. **Clona este repositorio (opcional):**

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Instala las bibliotecas necesarias**:

   Ejecuta el siguiente comando para instalar las bibliotecas requeridas:

   ```bash
   pip install transformers torch
   ```

## Preparación de Archivos de Texto

Antes de ejecutar el script, asegúrate de tener una carpeta llamada `archivos_texto` en el directorio raíz del proyecto. Esta carpeta debe contener algunos archivos de texto (`.txt`) con diferentes tipos de contenido.

Ejemplo:

- `archivos_texto/ciencia.txt`: Contenido relacionado con ciencia (física, química, etc.).
- `archivos_texto/tecnologia.txt`: Contenido relacionado con tecnología (computadoras, IA, etc.).

## Ejecución del Script

Para ejecutar el script, utiliza el siguiente comando:

```bash
python renombrar_archivos.py
```

Esto analizará cada archivo en la carpeta `archivos_texto` y los renombrará con un prefijo que indique el tema principal identificado por el clasificador de IA.

## Ejemplo de Uso

Si tienes un archivo llamado `historia.txt` en la carpeta `archivos_texto` que contiene información sobre eventos históricos, el script renombrará automáticamente el archivo a algo como:

```
historia_historia.txt
```

Cada archivo obtendrá un prefijo de tema, lo que hace que la organización de los archivos sea más clara y eficiente.

## Notas

- El script utiliza un clasificador "zero-shot", lo que significa que no requiere un entrenamiento específico para identificar temas comunes.
- Puedes editar la lista de temas en el script para adaptarla mejor a tus necesidades.

## Contribución

Si deseas contribuir al proyecto, siéntete libre de crear una bifurcación (fork) y enviar tus propuestas de mejoras.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT.

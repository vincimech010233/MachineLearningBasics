import os
from transformers import pipeline

# Crear un modelo de procesamiento de lenguaje natural
classifier = pipeline("zero-shot-classification")

# Definir una lista de temas para categorizar
temas = ["ciencia", "tecnología", "historia", "deportes", "arte", "literatura"]

# Carpeta donde están los archivos de texto
carpeta = "archivos_texto"

def renombrar_archivos(carpeta, temas):
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            ruta_archivo = os.path.join(carpeta, archivo)
            
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                contenido = f.read()
            
            resultado = classifier(contenido, temas)
            tema_principal = resultado['labels'][0]
            
            nuevo_nombre = f"{tema_principal}_{archivo}"
            nueva_ruta = os.path.join(carpeta, nuevo_nombre)
            os.rename(ruta_archivo, nueva_ruta)
            print(f"Renombrado: {archivo} -> {nuevo_nombre}")

renombrar_archivos(carpeta, temas)

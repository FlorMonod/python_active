# Script de procesamiento de datos en lote
# Enfocado en limpieza y estructuras clave-valor

import json

def estructurarPromptUsuario(nombre, rol, consulta):
    """
    Función que recibe los datos básicos de un usuario 
    y los estructura en formato diccionario (JSON).
    """
    return {
        "usuario": nombre.strip().title(),
        "perfil": rol.strip(),
        "consulta": consulta.strip(),
        "estado": "Activo"
    }

# Lista de usuarios simulando datos de entrada (lote)
entradasCrudas = [
    (" Florencia Monod  ", "Data Scientist", "¿Cómo se estructuran los datos para una base vectorial?"),
    (" Andres Rodrigues  ", "Data Analyst Jr.", "Optimización de consultas SQL en MySQL"),
    (" Maria Nuñez", "Automation Engineer", "Integración de webhooks con n8n")
]

# Se procesa la lista usando una list comprehensions 
datosProcesados = [
    estructurarPromptUsuario(nombre, rol, consulta) 
    for nombre, rol, consulta in entradasCrudas
]

# Se muestra el resultado en lote convertido a formato JSON legible
print("--- LOTE DE DATOS PROCESADOS PARA API ---")
print(json.dumps(datosProcesados, indent=4, ensure_ascii=False))
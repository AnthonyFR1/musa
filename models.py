from pydantic import BaseModel


# Definir un modelo de datos llamado Query que hereda de BaseModel
class Query(BaseModel):
    question: str   # Definir un campo llamado "question" que debe ser una cadena de texto (str)

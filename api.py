from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from haystack_utils import ask_question
from database import save_qa_record

# Crear un router APIRouter para definir endpoints de la API
router = APIRouter()

# Definir un modelo de Pydantic para las consultas de pregunta
class Query(BaseModel):
    question: str

# Definir un endpoint para el método GET en la ruta raíz "/"
# Este endpoint devuelve un mensaje de bienvenida al abrir la página
@router.get("/")
def read_root():
    return {"message": "¡Desafío Musache!"}


# Definir un endpoint para el método POST en la ruta "/ask"
# Este endpoint procesa las preguntas y devuelve respuestas
@router.post("/ask")
def ask_question_endpoint(query: Query):
    try:
        # Leer el contenido del archivo documento.txt que contiene el texto del documento
        with open("documentos/documento.txt", "r", encoding="utf-8") as file:
            document_text = file.read()
        
        # Obtener la respuesta a la pregunta utilizando la función ask_question
        answer = ask_question(query.question, document_text)
        
        # Si se encontró una respuesta, guardar el registro en la base de datos y devolver la respuesta
        if answer:
            save_qa_record(query.question, answer)
            return {"answer": answer}
        # Si no se encontró una respuesta, devolver un error HTTP 404
        else:
            raise HTTPException(status_code=404, detail="Lo siento, no encontré una respuesta para esa pregunta.")
    # Capturar cualquier excepción y devolver un error HTTP 500 con el detalle de la excepción
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

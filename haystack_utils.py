from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import DensePassageRetriever, FARMReader
from haystack.pipelines import ExtractiveQAPipeline


# Configurar el Document Store con Elasticsearch
document_store = ElasticsearchDocumentStore(host="localhost", username="", password="", index="document")

# Inicializar el Retriever y el Reader
retriever = DensePassageRetriever(
    document_store=document_store,
    query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
    passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base"
)


# Inicializar el Reader con el modelo preentrenado "deepset/roberta-base-squad2"
reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2")


# Crear un pipeline de QA utilizando el Reader y el Retriever inicializados
pipeline = ExtractiveQAPipeline(reader, retriever)


# Definir una función para hacer preguntas y obtener respuestas
def ask_question(query, document_text):
    if not query:  # Verificar si la pregunta está vacía
        return "Por favor, proporcione una pregunta válida."
    prediction = pipeline.run( #pipeline de QA para traer respuesta a partir de la pregunta y el texto del documento
        query=query,
        params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 1}}
    )
    answers = prediction['answers']
    
    # Verificar si se encontró alguna respuesta
    if answers:
        predicted_answer = answers[0].answer          # Obtener la respuesta predecida
        
        # Verificar si la respuesta está en el documento antes de devolverla
        if predicted_answer in document_text:
            return predicted_answer
        else:
            return "Lo siento, no encontré una respuesta relevante en el documento."
    else:
        return "Lo siento, no encontré una respuesta para esa pregunta."

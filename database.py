from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"        # URL de la base de datos SQLite

engine = create_engine(DATABASE_URL)      # Crear un motor de base de datos
Base = declarative_base()     # Crear una clase base declarativa para las definiciones de modelos


# Crear una sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Definir una clase de modelo para la tabla qa_records
class QARecord(Base):
    __tablename__ = "qa_records"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)    # Columna para almacenar preguntas
    answer = Column(Text)    # Columna para almacenar respuestas


# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(bind=engine)


# Función para guardar un registro de pregunta y respuesta en la base de datos
def save_qa_record(question, answer):       # Crear una nueva sesión de base de datos
    db = SessionLocal()         # Crear un nuevo registro QARecord con la pregunta y la respuesta
    record = QARecord(question=question, answer=answer)
    db.add(record)      # Agregar el registro a la sesión
    db.commit()       # Confirmar la transacción
    db.close()        # Cerrar la sesión

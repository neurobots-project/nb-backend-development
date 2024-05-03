from typing import List
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("crud_fastapi/secret.json")
firebase_admin.initialize_app(cred)

app = FastAPI()

db = firestore.client()

class Paciente(BaseModel):
    nome: str
    email: str
    telefone: str
    cep: str
    endereco: str
    cidade: str
    estado: str

# Rota para criar um paciente (CREATE)
@app.post("/pacientes/", status_code=status.HTTP_201_CREATED)
def criar_paciente(paciente: Paciente):
    doc_ref = db.collection("pacientes").add(paciente.model_dump())
    return {"mensagem": "Paciente criado com sucesso", "id": doc_ref.id}

# Rota para obter todos os pacientes (GET)
@app.get("/pacientes/", response_model=List[Paciente])
def obter_pacientes():
    pacientes = []
    docs = db.collection("pacientes").stream()
    for doc in docs:
        paciente_data = doc.to_dict()
        pacientes.append(Paciente(**paciente_data))
    return pacientes

# Rota para obter um paciente por ID (GET)
@app.get("/pacientes/{paciente_id}", response_model=Paciente)
def obter_paciente(paciente_id: str):
    doc_ref = db.collection("pacientes").document(paciente_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")
    paciente_data = doc.to_dict()
    return Paciente(**paciente_data)

# Rota para atualizar um paciente por ID (UPDATE)
@app.put("/pacientes/{paciente_id}", response_model=Paciente)
def atualizar_paciente(paciente_id: str, paciente: Paciente):
    doc_ref = db.collection("pacientes").document(paciente_id)
    doc_ref.set(paciente.model_dump())
    return Paciente(**paciente.model_dump(), id=paciente_id)

# Rota para deletar um paciente por ID (DELETE)
@app.delete("/pacientes/{paciente_id}")
def deletar_paciente(paciente_id: str):
    doc_ref = db.collection("pacientes").document(paciente_id)
    doc_ref.delete()
    return {"mensagem": "Paciente deletado com sucesso"}

# uvicorn crud_fastapi.main:app --reload
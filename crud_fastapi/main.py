from typing import List
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import firebase_admin
from firebase_admin import credentials, firestore
import uvicorn

cred = credentials.Certificate("crud_fastapi/secret.json")
firebase_admin.initialize_app(cred)

app = FastAPI(docs_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
                   )

db = firestore.client()

class Paciente(BaseModel):
    name: str
    email: str
    whatsapp: str
    city: str
    state: str
    hasAvc: str
    hasAnotherCondition: str
    investmentAmount: str

class Clinica(BaseModel):
    bairro: str
    cep: str
    cidade: str
    clinica: str
    contato: str
    email: str
    endereco_atendimento: str
    estado: str
    lat: str
    long: str
    pessoas: str
    profissao: str
    regiao: str

# Rota para criar um paciente (CREATE)
@app.post("/pacientes/add", status_code=status.HTTP_201_CREATED)
def criar_paciente(paciente: Paciente):
    doc_ref = db.collection("pacientes").add(paciente.dict())
    return {"mensagem": "Paciente criado com sucesso", "id": doc_ref[1].id}

# Rota para adicionar as clínicas ao banco de dados (POST)
@app.post("/clinicas/add", status_code=status.HTTP_201_CREATED)
def adicionar_clinicas():
    url = "https://api-clinics.rj.r.appspot.com/all"
    response = requests.get(url)
    
    if response.status_code == 200:
        clinicas_data = response.json()
        for clinica in clinicas_data:
            doc_ref = db.collection("clinicas").add(clinica)
        return {"mensagem": "Clínicas adicionadas com sucesso"}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao obter dados da API das clínicas")

# Rota para obter todos os pacientes (GET)
@app.get("/pacientes/", response_model=List[Paciente])
def obter_pacientes():
    pacientes = []
    docs = db.collection("pacientes").stream()
    for doc in docs:
        paciente_data = doc.to_dict()
        pacientes.append(Paciente(**paciente_data))
    return pacientes

# Rota para obter todas as clínicas (GET)
@app.get("/clinicas/", response_model=List[Clinica])
def obter_clinicas():
    clinicas = []
    docs = db.collection("clinicas").stream()
    for doc in docs:
        clinica_data = doc.to_dict()
        clinicas.append(Clinica(**clinica_data))
    return clinicas

# Rota para obter um paciente por ID (GET)
@app.get("/pacientes/{paciente_id}", response_model=Paciente)
def obter_paciente(paciente_id: str):
    doc_ref = db.collection("pacientes").document(paciente_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")
    paciente_data = doc.to_dict()
    return Paciente(**paciente_data)

# Rota para obter uma clínica por ID (GET)
@app.get("/clinicas/{clinica_id}", response_model=Clinica)
def obter_clinica(clinica_id: str):
    doc_ref = db.collection("clinicas").document(clinica_id)
    doc = doc_ref.get()
    if not doc.exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clínica não encontrada")
    clinica_data = doc.to_dict()
    return Clinica(**clinica_data)

# Rota para atualizar um paciente por ID (PUT)
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
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
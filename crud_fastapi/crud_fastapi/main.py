from typing import List
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import requests
import json

app = FastAPI()

linkDB = "https://residenciadb-7c712-default-rtdb.firebaseio.com/"

class Paciente(BaseModel):
    nome: str
    telefone: str
    cep: str
    endereco: str
    cidade: str
    estado: str

# Rota para criar um paciente
@app.post("/pacientes/", status_code=status.HTTP_201_CREATED)
def criar_paciente(paciente: Paciente):
    request = requests.post(f"{linkDB}/Pacientes/.json", data=json.dumps(paciente.model_dump()))
    if request.status_code != 200:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao criar paciente")
    return {"mensagem": "Paciente criado com sucesso"}

# Rota para obter todos os pacientes
@app.get("/pacientes/", response_model=List[Paciente])
def obter_pacientes():
    request = requests.get(f"{linkDB}/Pacientes/.json")
    if request.status_code != 200:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao obter pacientes")
    return [Paciente(**dados) for dados in request.json().values()]

# Rota para obter um paciente por ID
@app.get("/pacientes/{paciente_id}", response_model=Paciente)
def obter_paciente(paciente_id: str):
    request = requests.get(f"{linkDB}/Pacientes/{paciente_id}/.json")
    if request.status_code != 200:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Paciente não encontrado")
    return Paciente(**request.json())

# Rota para atualizar um paciente por ID
@app.put("/pacientes/{paciente_id}", response_model=Paciente)
def atualizar_paciente(paciente_id: str, paciente: Paciente):
    request = requests.put(f"{linkDB}/Pacientes/{paciente_id}/.json", data=json.dumps(paciente.model_dump()))
    if request.status_code != 200:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar paciente")
    return Paciente(**paciente.model_dump(), id=paciente_id)

# Rota para deletar um paciente por ID
@app.delete("/pacientes/{paciente_id}")
def deletar_paciente(paciente_id: str):
    request = requests.delete(f"{linkDB}/Pacientes/{paciente_id}/.json")
    if request.status_code != 200:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao deletar paciente")
    return {"mensagem": "Paciente deletado com sucesso"}

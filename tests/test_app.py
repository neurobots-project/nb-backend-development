import pytest
from fastapi.testclient import TestClient
from crud_fastapi.main import app
from fastapi import status

client = TestClient(app)

def test_criar_paciente():
    paciente_data = {
        "nome": "Percy",
        "email": "percyjackson@hotmail.com",
        "telefone": "81940023922",
        "cep": "52362-220",
        "endereco": "Rua numero dois",
        "cidade": "Recife",
        "estado": "PE"
    }
    response = client.post("/pacientes/add", json=paciente_data)
    
    assert response.status_code == 201
    responseJSON = response.json()
    assert "id" in responseJSON
    
    paciente_id = responseJSON["id"]
    
    response = client.get(f"/pacientes/{paciente_id}")
    assert response.status_code == 200
    
    paciente_response = response.json()
    assert paciente_response["nome"] == paciente_data["nome"]
    assert paciente_response["email"] == paciente_data["email"]
    assert paciente_response["telefone"] == paciente_data["telefone"]
    assert paciente_response["cep"] == paciente_data["cep"]
    assert paciente_response["endereco"] == paciente_data["endereco"]
    assert paciente_response["cidade"] == paciente_data["cidade"]
    assert paciente_response["estado"] == paciente_data["estado"]


def test_obter_pacientes():
    response = client.get("/pacientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_obter_paciente():
    # Este teste não irá criar um paciente no banco de dados
    response = client.get("/pacientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_atualizar_paciente():
    # Este teste não irá criar um paciente no banco de dados
    response = client.put(f"/pacientes/1", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_deletar_paciente():
    # Este teste não irá criar um paciente no banco de dados
    response = client.delete(f"/pacientes/1")
    assert response.status_code == status.HTTP_200_OK

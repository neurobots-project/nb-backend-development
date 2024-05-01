from typing import List
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Paciente(BaseModel):
   nome: str
   telefone: int  
   cep: str
   endereco: str
   cidade: str
   estado: str

database = []

# CREATE
@app.post(
   '/pacientes',
   response_model=Paciente,
   status_code=status.HTTP_201_CREATED,
   response_model_by_alias=False
)
def create_new_user(user: Paciente):
   database.append(user)
   return user

# READ
@app.get(
   '/pacientes',
   response_model=List[Paciente],
   status_code=status.HTTP_200_OK,
   response_model_by_alias=False
)
def get_all_users():
   return database

@app.get(
   '/pacientes/{id}',
   status_code=status.HTTP_200_OK,
   response_model_by_alias=False
)
def get_user_by_id(id: int):
   if id <= -1:
      raise HTTPException(
         status_code=status.HTTP_403_FORBIDDEN,
         detail="Id de paciente não permitido"
      )
   if not database[id] or len(database) < id:
      raise HTTPException(
         status_code=status.HTTP_404_NOT_FOUND,
         detail="Paciente não encontrado"
      )
   
   return database[id]

# UPDATE
@app.put(
   '/pacientes/{id}',
   response_model=Paciente,
   response_model_by_alias=False
)
def update_user_by_id(id: int, user_data: Paciente):
   if id <= -1:
      raise HTTPException(
         status_code=status.HTTP_403_FORBIDDEN,
         detail="Id de paciente não permitido"
      )
   if not database[id] or len(database) < id:
      raise HTTPException(
         status_code=status.HTTP_404_NOT_FOUND,
         detail="Paciente não encontrado"
      )
   
   database[id] = user_data
   return user_data

# DELETE
@app.delete(
   '/pacientes/{id}',
   status_code=status.HTTP_204_NO_CONTENT
)
def delete_user_by_id(id: int):
   if id <= -1:
      raise HTTPException(
         status_code=status.HTTP_403_FORBIDDEN,
         detail="Id de paciente não permitido"
      )
   if not database[id] or len(database) < id:
      raise HTTPException(
         status_code=status.HTTP_404_NOT_FOUND,
         detail="Paciente não encontrado"
      )
   
   del database[id]
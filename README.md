## CRUD API para Pacientes e Clínicas com FastAPI e Firebase

Este projeto implementa uma API RESTful utilizando FastAPI para gerenciar dados de pacientes e clínicas, armazenando-os no Firestore do Google Cloud.

### Funcionalidades:

* **CRUD (Create, Read, Update, Delete) para Pacientes:**
    * **Criar Paciente:** Permite criar um novo paciente com informações como nome, email, telefone, endereço, etc.
    * **Obter Pacientes:** Permite buscar todos os pacientes cadastrados ou um paciente específico por ID.
    * **Atualizar Paciente:** Permite atualizar os dados de um paciente existente por ID.
    * **Deletar Paciente:** Permite remover um paciente por ID.
* **CRUD para Clínicas:**
    * **Adicionar Clínicas:** Realiza a adição de várias clínicas ao banco de dados a partir de uma API externa.
    * **Obter Clínicas:** Permite buscar todas as clínicas cadastradas ou uma clínica específica por ID.
* **Validação de Dados:** Utiliza a biblioteca Pydantic para validar os dados de entrada das requisições.
* **Tratamento de Erros:** Implementa o tratamento de erros HTTP para lidar com casos como dados inválidos ou recursos não encontrados.
* **Documentação:** Utiliza a documentação automática do FastAPI para gerar documentação interativa da API.

### Instalação e Execução:
1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
2. **Configure a chave da API do firebase:**
   
    Insira dentro da pasta _crud_fastapi_ o arquivo secret.json.
3. **Execute a aplicação no terminal:**
   ```bash
   uvicorn crud_fastapi.main:app --reload

4. **Acesse a API:**

    A API estará disponível em http://127.0.0.1:8000/docs

### Arquitetura:
  * **FastAPI:** Framework Python para a construção de APIs RESTful.
  * **Firestore:** Banco de dados NoSQL do Google Cloud para armazenar os dados.
  * **Pydantic:** Biblioteca para validação de dados e criação de modelos de dados.
  * **Requests:** Biblioteca para realizar requisições HTTP.
  * **Firebase Admin SDK:** SDK Python para interagir com o Firebase.

### Observações:

* O projeto depende de uma API externa para obter os dados das clínicas. A URL da API está definida na rota `/clinicas/add`.
* A chave de serviço do Firebase é armazenada no arquivo `secret.json`. É importante manter esse arquivo em segurança.

**Este README é um guia básico para o projeto. Para obter informações mais detalhadas sobre o código, consulte os arquivos de código-fonte.**

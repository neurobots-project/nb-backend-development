## CRUD API para Pacientes e Clínicas com FastAPI e Firebase

Este projeto implementa uma API RESTful utilizando FastAPI para gerenciar dados de pacientes e clínicas, armazenando-os no Firestore do Google Cloud.

### Como funciona?:

![Diagrama em branco](https://github.com/neurobots-project/nb-backend-development/assets/110141875/078d136d-fa20-43cb-ade5-7baf096e63bc)

* **Frontend:**
   * O frontend da API é desenvolvido com React. O frontend se comunica com a API através de requisições HTTP.
* **API:**
   * A API é implementada com o framework FastAPI, que é um framework Python para a construção de APIs RESTful. A API expõe endpoints para realizar operações      CRUD em pacientes e clínicas.
* **ORM:**
   *  ORM (Object-Relational Mapper) é responsável por mapear objetos Python para entidades no banco de dados. No caso deste projeto, o ORM é utilizado para        mapear objetos Paciente e Clinica para documentos no Firestore.
* **Banco de Dados:**
   * O banco de dados utilizado para armazenar os dados dos pacientes e clínicas é o Firestore, que é um banco de dados NoSQL do Google Cloud.
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

### Deploy no Google Cloud:

A API está implantada no serviço Google Cloud, proporcionando alta disponibilidade, escalabilidade e integração perfeita com o Firestore. Esta implementação garante que a API possa lidar com um grande volume de solicitações de forma eficiente e segura.

### Instalação e Execução:
1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
2. **Execute a aplicação no terminal:**
   ```bash
   uvicorn crud_fastapi.main:app --reload

### Arquitetura:
  * **FastAPI:** Framework Python para a construção de APIs RESTful.
  * **Firestore:** Banco de dados NoSQL do Google Cloud para armazenar os dados.
  * **Pydantic:** Biblioteca para validação de dados e criação de modelos de dados.
  * **Requests:** Biblioteca para realizar requisições HTTP.
  * **Firebase Admin SDK:** SDK Python para interagir com o Firebase.

### Observações:

* O projeto depende de uma API externa para obter os dados das clínicas. A URL da API está definida na rota `/clinicas/add`.
* A chave de serviço do Firebase é armazenada no arquivo `secret.json`. É importante manter esse arquivo em segurança.

### Contribuidores:
* <a href="https://github.com/brunolcs1">**Bruno de Lucas**</a>
   * Responsável pelo deploy da aplicação
* <a href="https://github.com/lohhan">**Lohhan Guilherme**</a>
   * Responsável pela criação da API, interligação com o Banco de Dados e interligação com o Frontend.
* <a href="https://github.com/DevLucasKaua">**Lucas Kauã**</a>
   * Responsável pela documentação do projeto.
* <a href="https://github.com/JordanaTavares">**Jordana Tavares**</a>
   * Responsável pela interligação da API com o Frontend.
* <a href="https://github.com/Jricardoqc">**João Ricardo**</a>
   * Responsável pela interligação da API com o Frontend.
* <a href="https://github.com/LucasMen0r">**Lucas Menor**</a>
   * Responsável pela documentação do projeto.
* <a href="https://github.com/PauloHenriquebds">**Paulo Henrique**</a>
   * Responsável pelo deploy da aplicação.
* <a href="https://github.com/RafaelS-Silva">**Rafael Silva**</a>
   * Responsável pela documentação do projeto.
* <a href="https://github.com/WellersonMorais">**Wellerson Morais**</a>
   * Responsável pela documentação do projeto.
* <a href="https://github.com/willsilvaaa">**William Silva**</a>
   * Responsável pelos testes da aplicação.
     
<br>

**Este README é um guia básico para o projeto. Para obter informações mais detalhadas sobre o código, consulte os arquivos de código-fonte.**

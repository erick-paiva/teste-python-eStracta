# Company API

Este projeto implementa uma API para o gerenciamento de empresas, permitindo criar, ler, atualizar e deletar registros de empresas. Além disso, utiliza autenticação via JWT para proteger rotas.

## Funcionalidades

- **Autenticação JWT**: Protege as rotas da API, permitindo que apenas usuários autenticados realizem operações de CRUD.
- **CRUD de Empresas**: A API suporta operações completas de CRUD sobre empresas.
- **Swagger UI**: A API oferece uma documentação interativa via Swagger, acessível através de uma interface web.

## Tecnologias Utilizadas

- **Python 3.x**
- **Flask**
- **PostgreSQL**
- **Flask-SQLAlchemy** (ORM para banco de dados)
- **Flask-Migrate** (migrações de banco de dados)
- **JWT (JSON Web Token)** (para autenticação)
- **Swagger UI** (para documentação da API)

## Configuração do Projeto

### Pré-requisitos

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **PostgreSQL**: [Download PostgreSQL](https://www.postgresql.org/download/)
- **pipenv** ou **virtualenv** (opcional): Para criar um ambiente virtual.

### Passos para rodar o projeto

1. **Clonar o repositório**:

   Clone o repositório do projeto para o seu ambiente local:

   ```bash
   git clone https://github.com/erick-paiva/teste-python-eStracta
   cd teste-python-eStracta
   ```

2. **Criar um ambiente virtual**:

   Recomenda-se o uso de um ambiente virtual para gerenciar as dependências do projeto:

   ```bash
   # Usando venv
   python3 -m venv venv
   source venv/bin/activate  # No Windows: `venv\Scripts\activate`

   # Alternativamente, usando pipenv
   pipenv shell
   ```

3. **Instalar dependências**:

   Instale as dependências do projeto listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variáveis de ambiente**:

   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de configuração:

   ```env
   FLASK_ENV=development
   SECRET_KEY=sua_chave_secreta
   DATABASE_URL=postgresql://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>
   ```

   - **FLASK_ENV**: Define o ambiente de desenvolvimento.
   - **SECRET_KEY**: Chave secreta usada pelo Flask para sessões e JWT.
   - **DATABASE_URL**: URL de conexão com o banco de dados PostgreSQL.

5. **Configurar o banco de dados**:

   Certifique-se de que o PostgreSQL está rodando. Em seguida, crie o banco de dados e aplique as migrações:

   ```bash
   # Criar o banco de dados no PostgreSQL
   psql -U <usuario> -c "CREATE DATABASE <nome_do_banco>;"

   # Aplicar as migrações do banco de dados
   flask db upgrade
   ```

6. **Executar a aplicação**:

   Execute o servidor Flask:

   ```bash
   python app.py
   ```

   A API estará disponível em `http://localhost:5000/`.

7. **Acessar a documentação via Swagger**:

   Acesse a documentação interativa da API no navegador através de:

   ```
   http://localhost:5000/documentation/
   ```

8. **Autenticar na API**:

   Para acessar as rotas protegidas, você precisa de um token JWT. Faça uma requisição `POST` para a rota `/companies/login` com o seguinte corpo:

   ```json
   {
     "username": "admin",
     "password": "password"
   }
   ```

   A resposta será um token JWT. Use esse token nas requisições protegidas.

## Rotas da API

- `POST /companies/login`: Faz login e retorna um token JWT.
- `GET /companies/`: Lista todas as empresas com paginação, ordenação e busca por nome.
- `POST /companies/`: Cria uma nova empresa (rota protegida).
- `PUT /companies/{cnpj}`: Atualiza uma empresa existente (rota protegida).
- `DELETE /companies/{cnpj}`: Remove uma empresa (rota protegida).

## Exemplo de Requisição

### Buscar empresas pelo nome:

Faça uma requisição `GET` para `/companies/` com o nome da empresa como parâmetro de busca:

```bash
curl -X GET "http://localhost:5000/companies?name=Acme" -H "Authorization: <seu_token_jwt>"
```

### Criar uma nova empresa:

Faça uma requisição `POST` para `/companies/` com o token JWT obtido na autenticação, sem necessidade de prefixo `Bearer`:

```bash
curl -X POST http://localhost:5000/companies/ -H "Authorization: <seu_token_jwt>" -H "Content-Type: application/json" -d '{
  "cnpj": "12345678000199",
  "legal_name": "Acme Corp",
  "trade_name": "Acme",
  "cnae": "62010"
}'
```

### Atualizar uma empresa:

Faça uma requisição `PUT` para `/companies/{cnpj}`:

```bash
curl -X PUT http://localhost:5000/companies/12345678000199 -H "Authorization: <seu_token_jwt>" -H "Content-Type: application/json" -d '{
  "trade_name": "Acme Internacional",
  "cnae": "62020"
}'
```

### Deletar uma empresa:

Faça uma requisição `DELETE` para `/companies/{cnpj}`:

```bash
curl -X DELETE http://localhost:5000/companies/12345678000199 -H "Authorization: <seu_token_jwt>"
```

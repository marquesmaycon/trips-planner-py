# Trips Planner API

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-API-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

API em Flask para planejar viagens com convidados, confirmacoes, links uteis e atividades. O projeto organiza a regra de negocio em controllers e repositories, mantendo a persistencia em SQLite.

## Visao geral

- Criacao e consulta de viagens.
- Confirmacao de viagem e participantes.
- Cadastro de convidados por e-mail.
- Registro de links importantes da viagem.
- Cadastro e listagem de atividades por roteiro.
- Estrutura separada em rotas, controllers, drivers e repositories.

## Stack

| Camada | Tecnologia |
| --- | --- |
| Backend | Python, Flask |
| Banco de dados | SQLite |
| Arquitetura | Controllers, repositories e drivers |
| E-mail | SMTP para envio de confirmacoes |

## Estrutura

```text
.
|-- init/schema.sql
|-- run.py
|-- src/
|   |-- controllers/
|   |-- drivers/
|   |-- main/
|   |   |-- routes/
|   |   `-- server/
|   `-- models/
|       |-- repositories/
|       `-- settings/
```

## Como executar

```bash
python -m venv venv
source venv/bin/activate
pip install flask requests
python run.py
```

No Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install flask requests
python run.py
```

A API sobe em:

```text
http://localhost:3000
```

## Banco de dados

O projeto usa `storage.db` na raiz do repositorio. Para recriar o schema:

```bash
sqlite3 storage.db ".read init/schema.sql"
```

## Endpoints principais

| Metodo | Rota | Descricao |
| --- | --- | --- |
| POST | `/trips` | Cria uma viagem |
| GET | `/trips/{tripId}` | Busca os detalhes de uma viagem |
| POST | `/trips/{tripId}/confirm` | Confirma uma viagem |
| POST | `/trips/{tripId}/links` | Adiciona um link util |
| GET | `/trips/{tripId}/links` | Lista links da viagem |
| POST | `/trips/{tripId}/invites` | Convida um participante |
| PATCH | `/participants/{participantId}/confirm` | Confirma um participante |
| GET | `/trips/{tripId}/participants` | Lista participantes |
| POST | `/trips/{tripId}/activities` | Cria uma atividade |
| GET | `/trips/{tripId}/activities` | Lista atividades |

## E-mail de teste

Use o arquivo `create_email.py` para gerar credenciais de teste no Ethereal:

```bash
python create_email.py
```

Depois configure as credenciais no driver de envio em `src/drivers/email_sender.py`.

## Autor

Feito por [Maycon Marques](https://github.com/marquesmaycon).

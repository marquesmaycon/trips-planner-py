## Trip Planner API

API Flask para planejar viagens com convidados, links uteis e atividades, armazenando dados em SQLite.

### Visao geral
- Rotas em [src/main/routes/trips_routes.py](src/main/routes/trips_routes.py) e servidor em [src/main/server/server.py](src/main/server/server.py).
- Persistencia no arquivo `storage.db`; esquema SQL em [init/schema.sql](init/schema.sql).
- Envio de email de confirmacao via [src/drivers/email_sender.py](src/drivers/email_sender.py) usando SMTP (ex.: Ethereal).

### Requisitos
- Python 3.11+ e `pip`.
- Opcional: CLI `sqlite3` para aplicar o schema.

### Setup rapido (Windows)
```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install flask requests
sqlite3 storage.db ".read init/schema.sql"
```

### Executar a API
```powershell
python run.py
```
- Servidor em `http://localhost:3000`.
- O `db_connection_handler` abre `storage.db` no mesmo diretorio.

### Endpoints principais
- POST `/trips`: cria viagem. Corpo: `{ destination, start_date, end_date, owner_name, owner_email, emails_to_invite?[] }`. Resposta 201: `{ id }`.
- GET `/trips/{tripId}`: detalhes da viagem. Resposta 200: `{ trip: { id, destination, start_date, end_date, status } }`.
- POST `/trips/{tripId}/confirm`: confirma viagem. Resposta 200 corpo nulo.
- POST `/trips/{tripId}/links`: cria link. Corpo: `{ link, title }`. Resposta 201: `{ link_id }`.
- GET `/trips/{tripId}/links`: lista links. Resposta 200: `{ links: [{ id, link, title }] }`.
- POST `/trips/{tripId}/invites`: cria participante e email de convite. Corpo: `{ name, email }`. Resposta 201: `{ participant_id }`.
- PATCH `/participants/{participantId}/confirm`: confirma participante. Resposta 200 corpo nulo.
- GET `/trips/{tripId}/participants`: lista participantes. Resposta 200: `{ participants: [{ id, name, is_confirmed, email }] }`.
- POST `/trips/{tripId}/activities`: cria atividade. Corpo: `{ title, occurs_at }`. Resposta 201: `{ activity_id }`.
- GET `/trips/{tripId}/activities`: lista atividades. Resposta 200: `{ activities: [{ id, title, occurs_at }] }`.

### Envio de email de teste
- Use [create_email.py](create_email.py) para gerar credenciais Ethereal: `python create_email.py`.
- Defina `my_email` e `password` em [src/drivers/email_sender.py](src/drivers/email_sender.py) com as credenciais retornadas.

### Dicas
- Para reiniciar o banco, delete `storage.db` e reexecute o comando do schema.
- Ajuste o host/porta em [run.py](run.py) se necessario.
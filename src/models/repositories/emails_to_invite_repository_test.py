import pytest
import uuid

# from datetime import datetime, timedelta
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

email_to_invite_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interação com o banco de dados")
def test_create_email_to_invite():
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)

  emails_to_invite_infos = {
    "id": email_to_invite_id,
    "email": "mayconmarquesh@gmail.com",
    "trip_id": trip_id
  }

  emails_to_invite_repository.create_email_to_invite(emails_to_invite_infos)

@pytest.mark.skip(reason="interação com o banco de dados")
def test_find_emails_from_trip():
  conn = db_connection_handler.get_connection()
  emails_to_invite_repository = EmailsToInviteRepository(conn)

  emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
  print()
  print(emails)

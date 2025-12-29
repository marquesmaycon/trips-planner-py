import uuid

from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

class ParticipantCreator:
  def __init__(self, participants_repository: ParticipantsRepository, emails_repository: EmailsToInviteRepository) -> None:
    self.__participants_repository = participants_repository
    self.__emails_repository = emails_repository
    
  def create(self, body, trip_id) -> dict:
    try:
      participant_id = str(uuid.uuid4())
      email_id = str(uuid.uuid4())
      
      emails_infos = {
        "id": email_id,
        "email": body['email'],
        "trip_id": trip_id,
      }
      
      participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": email_id,
        "name": body['name'],
      }
    
      self.__emails_repository.create_email_to_invite(emails_infos)
      self.__participants_repository.create_participant(participant_infos)
      
      return {
        "body": { "participant_id": participant_id },
        "status_code": 201
      }
    except Exception as e:
      return {
        "body": { "error": "Bad Request", "message": str(e) },
        "status_code": 400
      }
      
      
    
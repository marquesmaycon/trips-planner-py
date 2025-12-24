import uuid
from src.models.repositories.links_repository import LinksRepository

class LinkCreator:
  def __init__(self, links_repository: LinksRepository):
    self.links_repository = links_repository
  
  def create(self, body, trip_id) -> dict:
    try:
      link_id = str(uuid.uuid4())
      
      link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": body['link'],
        "title": body['title'],
      }
      
      self.links_repository.create_link(link_infos)
      
      return {
        "body": { "link_id": link_id },
        "status_code": 201
      }
    except Exception as e:
      return {
        "body": { "error": "Bad Request", "message": str(e) },
        "status_code": 404
      }    
  
        
  
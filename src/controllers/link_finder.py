from src.models.repositories.links_repository import LinksRepository

class LinkFinder:
  def __init__(self, link_repository: LinksRepository):
    self.link_repository = link_repository
  
  def find(self, trip_id) -> dict:
    try:
      links = self.link_repository.find_links_from_trip(trip_id)
      
      formatted_links = []
      
      for link in links:
        formatted_links.append({
          "id": link[0],
          "link": link[2],
          "title": link[3],
        })
      
      return {
        "body": { "links": formatted_links },
        "status_code": 200
      }
    except Exception as e:
      return {
        "body": { "error": "Bad Request", "message": str(e) },
        "status_code": 404
      }   
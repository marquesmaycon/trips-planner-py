from src.models.repositories.trips_repository import TripsRepository

class TripConfirmer:
  def __init__(self, trips_repository: TripsRepository):
    self.trips_repository = trips_repository
  
  def confirm(self, trip_id: str) -> dict:
    try:
      trip = self.trips_repository.find_trip_by_id(trip_id)
      if not trip: raise Exception("Trip not found")
      
      self.trips_repository.update_trip_status(trip_id, 1)
      
      return {
        "body": None,
        "status_code": 200
      }
    except Exception as e:
      return {
        "body": { "error": "Bad Request", "message": str(e) },
        "status_code": 404
      }    
  
        
  
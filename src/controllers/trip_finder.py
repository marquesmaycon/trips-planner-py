from src.models.repositories.trips_repository import TripsRepository

class TripFinder:
  def __init__(self, trip_repository: TripsRepository):
    self.trip_repository = trip_repository

  def find_trip(self, trip_id):
    try:
      trip = self.trip_repository.find_trip_by_id(trip_id)
      if not trip: raise Exception("Trip not found") 
      
      return {
        "body": {
          "trip": {
            "id": trip[0],
            "destination": trip[1],
            "start_date": trip[2],
            "end_date": trip[3],
            "status": trip[6]
          }
        },
        "status_code": 200
      }
    except Exception as e:
      return {
        "body": { "error": "Bad Request", "message": str(e) },
        "status_code": 404
      }
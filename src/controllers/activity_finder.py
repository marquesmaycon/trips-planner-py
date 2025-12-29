from src.models.repositories.activities_repository import ActivitiesRepository

class ActivityFinder:
  def __init__(self, activities_repository: ActivitiesRepository):
    self.__activities_repository = activities_repository
    
  def find_from_trip(self, trip_id) -> dict:
    try:
     
      activities = self.__activities_repository.find_activities_from_trip(trip_id)
      
      formatted_activities = []
      for activity in activities:
        formatted_activities.append({
          "id": activity[0],
          "title": activity[2],
          "occurs_at": activity[3],
        })
        
      return {
        "body": { "activities": formatted_activities },
        "status_code": 200
      }
    except Exception as e:
      return {
        "body": { "error": "Bad Request", "message": str(e) },
        "status_code": 400
      }
      
      
    
from sqlite3 import Connection
from typing import List, Tuple

class ParticipantsRepository:
    
  def __init__(self, conn: Connection):
    self.conn = conn
    
  def create_participant(self, participant_infos: dict):
    cursor = self.conn.cursor()
    
    cursor.execute(
      """
        INSERT INTO participants 
          (id, trip_id, emails_to_invite_id, name)
        VALUES 
          (?, ?, ?, ?)
      """,
      (
        participant_infos["id"],
        participant_infos["trip_id"],
        participant_infos["emails_to_invite_id"],
        participant_infos["name"],
      )
    )
    
    self.conn.commit()
    
  def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
    cursor = self.conn.cursor()
    
    cursor.execute(
      """ 
        SELECT 
          p.id, p.name, p.is_confirmed, e.email 
        FROM participants as p 
        JOIN emails_to_invite as e 
          ON p.emails_to_invite_id = e.id
        WHERE trip_id = ? 
      """,
      (trip_id,)
    )
    
    rows = cursor.fetchall()
    
    participants = []
    for row in rows:
      participants.append({
        "id": row[0],
        "trip_id": row[1],
        "emails_to_invite_id": row[2],
        "name": row[3],
        "is_confirmed": bool(row[4]) if row[4] is not None else None,
      })
    
    return participants
  
  def update_participant_status(self, participant_id: str)-> None:
    cursor = self.conn.cursor()
    
    cursor.execute(
      """
        UPDATE participants 
        SET is_confirmed = 1 
        WHERE id = ?
      """,
      (participant_id,)
    )
    
    self.conn.commit()
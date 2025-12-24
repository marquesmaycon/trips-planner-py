import pytest
import uuid

# from datetime import datetime, timedelta
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
link_id = str(uuid.uuid4())
trip_id = str(uuid.uuid4())

# @pytest.mark.skip(reason="interação com o banco de dados")
def test_create_link():
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)

  link_infos = {
    "id": link_id,
    "link": "http://example.com",
    "trip_id": trip_id,
    "title": "Example Link"
  }

  links_repository.create_link(link_infos)


# @pytest.mark.skip(reason="interação com o banco de dados")
def test_find_links_from_trip():
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)

  links = links_repository.find_links_from_trip(trip_id)
  print()
  print(links)

  assert isinstance(links, list)
  assert isinstance(links[0], tuple)
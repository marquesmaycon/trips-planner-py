from flask import jsonify, Blueprint, request

from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
  conn = db_connection_handler.get_connection()
  
  trips_repository = TripsRepository(conn)
  emails_to_invite_repository = EmailsToInviteRepository(conn)
  controller = TripCreator(trips_repository, emails_to_invite_repository)

  resp = controller.create(request.json)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def get_trip(tripId):
  conn = db_connection_handler.get_connection()
  
  trips_repository = TripsRepository(conn)
  controller = TripFinder(trips_repository)

  resp = controller.find_trip(tripId)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["POST"])
def confirm_trip(tripId):
  conn = db_connection_handler.get_connection()
  
  trips_repository = TripsRepository(conn)
  controller = TripConfirmer(trips_repository)
  
  resp = controller.confirm(tripId)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_link(tripId):
  conn = db_connection_handler.get_connection()
  
  links_repository = LinksRepository(conn)
  controller = LinkCreator(links_repository)
  
  resp = controller.create(request.json, tripId)
  
  return jsonify(resp["body"]), resp["status_code"]
from flask import jsonify, Blueprint, request

from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.activity_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder

from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer

from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

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

@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_links(tripId):
  conn = db_connection_handler.get_connection()
  
  links_repository = LinksRepository(conn)
  controller = LinkFinder(links_repository)
  
  resp = controller.find(tripId)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):
  conn = db_connection_handler.get_connection()
  
  participant_repository = ParticipantsRepository(conn)
  emails_to_invite_repository = EmailsToInviteRepository(conn)
  controller = ParticipantCreator(participant_repository, emails_to_invite_repository)
  
  resp = controller.create(request.json, tripId)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def create_activity(tripId):
  conn = db_connection_handler.get_connection()
  
  activities_repository = ActivitiesRepository(conn)
  controller = ActivityCreator(activities_repository)
  
  resp = controller.create(request.json, tripId)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def get_trip_participants(tripId):
  conn = db_connection_handler.get_connection()
  
  participants_repository = ParticipantsRepository(conn)
  controller = ParticipantFinder(participants_repository)
  
  resp = controller.find_participants_from_trip(tripId)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
  conn = db_connection_handler.get_connection()
  
  activities_repository = ActivitiesRepository(conn)
  controller = ActivityFinder(activities_repository)
  
  resp = controller.find_from_trip(tripId)
  
  return jsonify(resp["body"]), resp["status_code"]

@trips_routes_bp.route("/participants/<participantId>/confirm", methods=["PATCH"])
def confirm_participant(participantId):
  conn = db_connection_handler.get_connection()
  
  participant_repository = ParticipantsRepository(conn)
  controller = ParticipantConfirmer(participant_repository)
  
  resp = controller.confirm(participantId)
  
  return jsonify(resp["body"]), resp["status_code"]


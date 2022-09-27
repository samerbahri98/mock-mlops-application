from flask import jsonify, request
from flask.blueprints import Blueprint
from init import init
from decorators import with_portainer
from db import logger_cursor

api = Blueprint('api', __name__)


### PULL LOGS
@api.route("/logs", methods=["GET"])
def pull():
    logger_cursor.execute("select * from logs")
    logger_cursor_results = logger_cursor.fetchall()
    return jsonify([{
        "id": log[0],
        "branch": log[1],
        "name": log[2],
        "resourceVersion": log[3],
        "state": log[4],
        "created_at": log[5]
    } for log in logger_cursor_results])


### HEALTHCHECK
@api.route("/health", methods=["GET"])
@with_portainer
def healthcheck(jwt):
    init(jwt)
    return jsonify({"status": "live"})

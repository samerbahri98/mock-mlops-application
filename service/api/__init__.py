from flask import jsonify, request
from flask.blueprints import Blueprint
from init import init
from decorators import with_portainer

api = Blueprint('api', __name__)

### PUSH LOGS
@api.route("/",methods=["POST"])
def push():
    return 

### PULL LOGS
@api.route("/",methods=["GET"])
@with_portainer
def pull(jwt):
    return jsonify({"jwt":jwt})

### HEALTHCHECK
@api.route("/health",methods=["GET"])
@with_portainer
def healthcheck(jwt):
    init(jwt)
    return jsonify({"status":"live"})

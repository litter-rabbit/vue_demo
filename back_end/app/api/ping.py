
from flask import jsonify
from flask import Blueprint

api_bp=Blueprint('api',__name__)


@api_bp.route('/ping',methods=['GET'])
def ping():
    return jsonify('Pong')

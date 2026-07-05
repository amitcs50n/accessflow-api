from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.get("/health")
def health_checck():
    return jsonify({
        "status":"ok",
        "service":"AccessFlow API"
    })
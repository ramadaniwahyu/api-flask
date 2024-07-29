from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import secrets

db = SQLAlchemy()
BLOCKLIST = set()

from .resources.user import blp as UserBlueprint
from .resources.emp import blp as EmpBlueprint
from .resources.relaas import blp as RelaasBlueprint

def create_app():
    app = Flask(__name__)
      
    # Configuration of application, see configuration.py, choose one and uncomment.
    # app.config.from_object('config.ProductionConfig')
    app.config.from_object('config.DevelopmentConfig')
    # app.config.from_object('config.TestingConfig')
    
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    jwt = JWTManager(app)
    
    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        # TODO: Read from a config file instead of hard-coding
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}
    
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
        
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(EmpBlueprint)
    api.register_blueprint(RelaasBlueprint)
    
    return app
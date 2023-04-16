import os
import secrets

from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
import models
from resources.trka import blp as TrkaBlueprint
from resources.manifestacija import blp as ManifestacijaBlueprint
from resources.trkac import blp as TrkacBlueprint

from resources.android import blp as AndroidBlueprint
from resources.citac import blp as CitacBlueprint
from resources.negativni_poeni import blp as Negativni_poeniBlueprint
from resources.user import blp as UserBlueprint

from waitress import serve
#print("***********")
def create_app(db_url=None):
    app = Flask(__name__)
    #env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
    #app.config.from_object(env_config)
    #app.config["PROPAGATE_EXCEPTIONS"] = False
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
#    app.config['SERVERS'] = [
#        {
#            'name': 'Dev Server',
#            'url': 'http://127.0.0.1:5000'
#        },
#        {
#            'name': 'Production Server',
#            'url': 'http://trka.online'
#        }
#   ]
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "jose" #"100089503240687113175841716378207429919"
    #secrets.SystemRandom().getrandbits(128)
    jwt = JWTManager(app)


    with app.app_context():
        db.create_all()

    api.register_blueprint(TrkaBlueprint)
    api.register_blueprint(ManifestacijaBlueprint)
    api.register_blueprint(TrkacBlueprint)

    api.register_blueprint(AndroidBlueprint)
    api.register_blueprint(CitacBlueprint)
    api.register_blueprint(Negativni_poeniBlueprint)
    api.register_blueprint(UserBlueprint)


    return app
#mode = "prod"
#if __name__ == "__app__":
#print("--------------")
    #from waitress import serve
#if mode == "dev":
#    create_app.run(host='0.0.0.0', port = 50100, debug = True)
#else:
#    serve(create_app, host="0.0.0.0", port = 50100, threads = 1 )
#if __name__ == "__app__":
#    print("--------------")
#    from waitress import serve
#    serve(create_app, host="0.0.0.0", port=8080)




from flask import Flask
from flask_cors import CORS

# ROUTES

from routes.auth_routes import auth_bp
from routes.prediction_routes import prediction_bp
from routes.alert_routes import alert_bp
from routes.gis_routes import gis_bp
from routes.satellite_routes import satellite_bp

# CONFIG

from config.development import Config

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    # API ROUTES

    app.register_blueprint(

        auth_bp,

        url_prefix="/api/auth"

    )

    app.register_blueprint(

        prediction_bp,

        url_prefix="/api/prediction"

    )

    app.register_blueprint(

        alert_bp,

        url_prefix="/api/alerts"

    )

    app.register_blueprint(

        gis_bp,

        url_prefix="/api/gis"

    )

    app.register_blueprint(

        satellite_bp,

        url_prefix="/api/satellite"

    )

    @app.route("/")

    def home():

        return {

            "status":"Running",

            "project":

            "AI Disaster Prediction Backend"

        }

    return app


app = create_app()

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
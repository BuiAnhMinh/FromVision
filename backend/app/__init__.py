from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    # Enable Cross-Origin requests (so your frontend can call this API)
    CORS(app)

    # (Optional) configuration, e.g. upload folder
    # app.config['UPLOAD_FOLDER'] = 'uploads/'

    # Import and register your routes
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

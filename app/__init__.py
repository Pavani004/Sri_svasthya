from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Change this for security

    csrf.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app

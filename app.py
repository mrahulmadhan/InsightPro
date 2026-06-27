from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from routes.dashboard_routes import bp as dashboard_bp
    from routes.api_routes import bp as api_bp
    
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

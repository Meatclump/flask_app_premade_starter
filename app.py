from flask import Flask

from blueprints.views import views_bp

app = Flask(__name__)

app.register_blueprint(views_bp)

if __name__ == "__main__":
    app.run(debug=True)
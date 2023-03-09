from flask import Flask
import json
from blueprints.views import views_bp
import modules.db_interface as db_interface
settings = json.loads(open('config.json').read())

app = Flask(__name__)
app.config.update(settings)

app.register_blueprint(views_bp)

if __name__ == "__main__":
    app.run(debug=True)
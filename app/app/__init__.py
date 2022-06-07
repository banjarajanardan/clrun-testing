from flask import Flask
from flask_cors import CORS
from loguru import logger

from .main import qna_blueprint

logger.debug("Starting Server")
app = Flask(__name__)
CORS(app)

url_prefix = "/api/v1"

logger.debug("Loading Blueprints")
app.register_blueprint(qna_blueprint, url_prefix=url_prefix)

if __name__ == "__main__":
    app.run(port=8000)

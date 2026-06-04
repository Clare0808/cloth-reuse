from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from api import api_bp
from database import init_db
from flask_jwt_extended import JWTManager
import os
from api.login import init_admin
from extensions import socketio

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # 根目錄
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'upload')

# app = Flask(__name__, static_url_path='/upload', static_folder=UPLOAD_FOLDER, template_folder="templates")
app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates') # add
init_db(app)
CORS(app, origins="*") # 允許前端從發送請求

app.config["JWT_SECRET_KEY"] = "6011f54da74acdb140a481f2a4ba57adc9e73429508cb9333e78945332baa1d9"
jwt = JWTManager(app)

socketio.init_app(app, cors_allowed_origins="*")

app.register_blueprint(api_bp, url_prefix="/api") # 將 API 藍圖註冊到 app 中

with app.app_context():
    init_admin()

# add
@app.route('/upload/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/data/<path:filename>')
def data_file(filename):
    return send_from_directory(os.path.join(app.static_folder, 'data'), filename)

@app.route('/img/cloth/<path:filename>')
def cloth_image(filename):
    return send_from_directory(os.path.join(app.static_folder, 'img', 'cloth'), filename)

@app.route("/")
@app.route("/<path:path>")
def index(path=None):
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) # add
    # socketio.run(app, port=5000, debug=True)
    socketio.run(app, host="0.0.0.0", port=port, debug=False) # add

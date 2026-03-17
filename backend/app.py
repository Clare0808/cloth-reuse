from flask import Flask
from flask_cors import CORS
from api import api_bp
from database import init_db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
init_db(app)
CORS(app, origins="*") # 允許前端從發送請求

app.register_blueprint(api_bp, url_prefix="/api") # 將 API 藍圖註冊到 app 中

app.config["JWT_SECRET_KEY"] = "6011f54da74acdb140a481f2a4ba57adc9e73429508cb9333e78945332baa1d9" 
jwt = JWTManager(app)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
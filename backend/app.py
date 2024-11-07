from flask import Flask, Blueprint
from flask_migrate import Migrate
from config import Config
from models import db
from routes.user_routes import user_api
from routes.goal_routes import goal_api
from routes.transaction_routes import transaction_api
from flask_cors import CORS

# Khởi tạo ứng dụng Flask
app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Khởi tạo cơ sở dữ liệu và migration
db.init_app(app)
migrate = Migrate(app, db)

# Đăng ký blueprint cho route
api_blueprint = Blueprint('api', __name__, url_prefix='/api')

# Đăng ký các Blueprint con vào api_blueprint
app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(goal_api, url_prefix='/api/goal')
app.register_blueprint(transaction_api, url_prefix='/api/transaction')

if __name__ == '__main__':
    app.run(debug=True)

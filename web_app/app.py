from flask import Flask, request, jsonify, url_for, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, current_user
import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

import config_app as config_app
from models import User, db

app = Flask(__name__, template_folder='templates')
app.config.from_object(config_app)
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

from user_app import user


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

app.register_blueprint(user, url_prefix='/user')
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
def main():
    app.run(debug=True, port=8000, host='0.0.0.0')

if __name__ == '__main__':
    main()
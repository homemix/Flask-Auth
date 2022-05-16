from flask import Flask
from blueprints.AuthBluePrint import auth
from blueprints.MainBluePrint import main
from database import db
from flask_login import LoginManager
import models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


app.register_blueprint(auth)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run()

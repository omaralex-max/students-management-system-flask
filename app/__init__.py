from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_options
from app.model import db

def create_app(config_name='dev'):

    app = Flask(__name__)

    current_config = config_options[config_name]


    app.config.from_object(current_config)

    db.init_app(app) 
    
    from app.students.views import index

    app.add_url_rule('/students', view_func=index , endpoint='/students.index')
    
    return app  
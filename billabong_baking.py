import sqlalchemy as sa
import sqlalchemy.orm as so
from flask import Blueprint
from app import db, create_app
from app.models import User, Post, Recipe

#app = create_app()
bp = Blueprint('auth', __name__)

@bp.app_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post, 'Recipe': Recipe}
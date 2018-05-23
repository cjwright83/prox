from flask import Blueprint, render_template
from proxysql import db

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/')
def list():
    return render_template(
        'users/index.html',
        users=db.fetch_all_from_table('mysql_users')
    )

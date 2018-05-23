from flask import Blueprint, render_template
from proxysql import db

servers = Blueprint('servers', __name__, template_folder='templates')


@servers.route('/')
def list():
    return render_template(
        'servers/index.html',
        servers=db.fetch_all_from_table('mysql_servers')
    )

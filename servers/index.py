from flask import Blueprint, render_template
from connection import mysql

servers = Blueprint('servers', __name__, template_folder='templates')


@servers.route('/')
def list():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * from mysql_servers')
    return render_template('servers/index.html', servers=cursor.fetchall())

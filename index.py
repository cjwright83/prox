import os

from flask import Flask
from flask import render_template

from dotenv import load_dotenv

from connection import mysql
from servers.index import servers

app = Flask(__name__)
load_dotenv()

app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT'))

mysql.init_app(app)
app.register_blueprint(servers, url_prefix='/servers')


@app.route('/')
def hello_world():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * from mysql_query_rules')
    rules = cursor.fetchall()
    cursor.execute('SELECT * from mysql_servers')
    servers = cursor.fetchall()
    cursor.execute('SELECT * from mysql_users')
    users = cursor.fetchall()
    return render_template('index.html', rules=rules, servers=servers, users=users)

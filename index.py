import os

from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

from dotenv import load_dotenv

app = Flask(__name__)
mysql = MySQL()
load_dotenv()

app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_NAME')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('DB_PORT'))
mysql.init_app(app)


@app.route('/')
def hello_world():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * from mysql_query_rules')
    rs = cursor.fetchall()
    return render_template('index.html', rules=rs)

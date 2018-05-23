from flask import Flask
from flask import render_template

from dotenv import load_dotenv

from rules.index import rules
from servers.index import servers
from users.index import users

app = Flask(__name__)
load_dotenv()

app.register_blueprint(rules, url_prefix='/rules')
app.register_blueprint(servers, url_prefix='/servers')
app.register_blueprint(users, url_prefix='/users')


@app.route('/')
def index():
    return render_template('index.html')

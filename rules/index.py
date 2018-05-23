from flask import Blueprint, render_template
from proxysql import db

rules = Blueprint('rules', __name__, template_folder='templates')


@rules.route('/')
def list():
    return render_template(
        'rules/index.html',
        rules=db.fetch_all_from_table('mysql_query_rules')
)

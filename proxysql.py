import os

import pymysql


class Database(object):
    def __init__(self, connection):
        self.connection = connection

    def fetch_all_from_table(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM {}'.format(table_name))
        columns = [column[0] for column in cursor.description]
        resultset = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return resultset


db = Database(connection=pymysql.connect(
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME')
))

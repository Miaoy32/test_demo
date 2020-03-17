#encoding: utf-8

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_migrate_demo'
USERNAME = 'root'
PASSWORD = ''

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,
                                                 DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
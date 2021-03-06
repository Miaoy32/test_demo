#encoding: utf-8

from flask_script import  Manager
from flask_migrate_demo import app
from flask_migrate import MigrateCommand,Migrate
from exts import db
from models import User

manager = Manager(app)
Migrate(app,db)
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()

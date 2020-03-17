from flask import Flask,render_template
import config
from models import User
from exts import db
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def hello_world():

    return 'Hello World!'


@app.route('/user/')
def user():
    users = User.query.all()
    return render_template('user.html',users=users)


if __name__ == '__main__':
    app.run(port=9000)

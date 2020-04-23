from flask import Flask, request, render_template, Response, session, redirect, url_for, redirect, flash
from scripts.alg import algorithm
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'music'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'


class User(UserMixin, db.Model):
    """Model for user accounts."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    result = db.relationship('Status', backref='answer')


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String, nullable=False, unique=False)
    date = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/main', methods=['POST', 'GET'])
def main():
    answer = []
    if request.method == 'POST':
        r1 = request.form['location']
        r2 = request.form['action']
        r3 = request.form['sign']
        r4 = request.form['mood']
        r5 = request.form['age']

        result = [r1, r2, r3, r4, r5]
        answer = algorithm(result)

        if len(answer) > 1:
            answer = str(answer)
        else:
            answer = answer[0]

        if current_user.is_authenticated:
            date = datetime.datetime.now()
            session = Status(result = answer.capitalize(), date = date, user_id = current_user.id)
            db.session.add(session)
            db.session.commit()
        return render_template('resultpage.html', answer=answer)
    return render_template('index.html', answer=answer)


@app.route('/results')
def results():
    return render_template('resultpage.html')


@app.route('/about', methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('User Created', 'success')
        return render_template('about.html')
    return render_template('about.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            if user.password == request.form['password']:
                login_user(user)
                flash('Login Successful', 'success')
                return redirect(url_for('main'))
            else:
                flash('User/Password is wrong', 'danger')
    return render_template('login.html')


@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    list = []
    session = Status.query.filter_by(user_id=current_user.id)
    for s in session:
        list.append(s)
    return render_template('profile.html', list = list)


if __name__ == "__main__":
    app.run(debug=True)

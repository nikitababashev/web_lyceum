from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask import Flask, request, url_for, redirect, render_template
from data import db_session
from data.users import User
from flask_login import LoginManager, logout_user, login_user, login_required


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


db_session.global_init("db/profiles.db")


login_manager = LoginManager()
login_manager.init_app(app)


class EnterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surename = StringField('Фамилия', validators=[DataRequired()])
    pochta = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


user_email = 'none@yandex.ru'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    global user_email
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.surename = form.surename.data
        user.email = form.pochta.data
        user.reyting = '0'
        user.set_password(form.password.data)
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        user_email = form.pochta.data
        return redirect('/success')
    return f"""<!doctype html>
                            <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Решалкин</title>
                                </head>
                                <body>
                                    <div class="alert alert-primary" role="alert">
                                        Сайт по подготовке к ЕГЭ и ОГЭ: "Решалкин".
                                    </div>
                                    <h2>Пожалуйста зарегистрируйтесь.</h2>
                                    {render_template('login.html', form=form)}
                                    <a href="/enter">уже зарегистрировались?</a>
                                </body>
                            </html>"""


@app.route('/enter', methods=['GET', 'POST'])
def enter():
    global user_email
    form = EnterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            user_email = form.email.data
            return redirect("/success")
        return f"""<!doctype html>
                            <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Решалкин</title>
                                </head>
                                <body>
                                    <div class="alert alert-primary" role="alert">
                                        Сайт по подготовке к ЕГЭ и ОГЭ: "Решалкин".
                                    </div>
                                    <h2>Пожалуйста войдите в аккаунт.</h2>
                                    {render_template('login.html', message="Неправильный логин или пароль", form=form)}
                                </body>
                            </html>"""
    return f"""<!doctype html>
                            <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                    <title>Решалкин</title>
                                </head>
                                <body>
                                    <div class="alert alert-primary" role="alert">
                                        Сайт по подготовке к ЕГЭ и ОГЭ: "Решалкин".
                                    </div>
                                    <h2>Пожалуйста войдите в аккаунт.</h2>
                                    {render_template('login.html', form=form)}
                                </body>
                            </html>"""


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/enter')


@app.route('/success')
def success():
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == user_email).first()
    return f"""<!doctype html>
                                <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                        <link rel="stylesheet"
                                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                        crossorigin="anonymous">
                                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                        <title>Решалкин</title>
                                    </head>
                                    <body>
                                        <div class="alert alert-primary" role="alert">
                                            Сайт по подготовке к ЕГЭ и ОГЭ: "Решалкин".
                                        </div>
                                        <h2>Здравствуйте, {user.name}!</h2>
                                        <a href="/tasks">Задачи</a>
                                        <a href="/profile">Профиль</a>
                                        <p style="position:absolute;right:0;bottom:0;margin-bottom:0">
                                            <a href="/logout">выйти из аккаунта</a>
                                        </p>
                                    </body>
                                </html>"""


@app.route('/profile')
def profile():
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.email == user_email).first()
    return f"""<!doctype html>
                                    <html lang="en">
                                        <head>
                                            <meta charset="utf-8">
                                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                            <link rel="stylesheet"
                                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                            crossorigin="anonymous">
                                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                            <title>Решалкин</title>
                                        </head>
                                        <body>
                                            <div class="alert alert-primary" role="alert">
                                                Сайт по подготовке к ЕГЭ и ОГЭ: "Решалкин".
                                            </div>
                                            {render_template('rect.html')}
                                            <div class="rectangle text_left">
                                                <h1>Ваш профиль:</h1>
                                                <h2>
                                                    Имя:{user.name}, Фамилия: {user.surename}
                                                </h2>
                                                <h3>Рейтинг:{user.reyting}</h3>
                                            </div>
                                        </body>
                                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
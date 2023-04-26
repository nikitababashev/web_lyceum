from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired
from flask import Flask, request, url_for, redirect, render_template
from data import db_session
from data.users import User
from flask_login import LoginManager, logout_user, login_user, login_required


db_session.global_init("db/profiles.db")


class SubForm(FlaskForm):
    answer1 = StringField('Ответ на 1 вопрос', validators=[DataRequired()])
    answer2 = StringField('Ответ на 2 вопрос', validators=[DataRequired()])
    answer3 = StringField('Ответ на 3 вопрос', validators=[DataRequired()])
    answer4 = StringField('Ответ на 4 вопрос', validators=[DataRequired()])
    answer5 = StringField('Ответ на 5 вопрос', validators=[DataRequired()])
    answer6 = StringField('Ответ на 6 вопрос', validators=[DataRequired()])
    answer7 = StringField('Ответ на 7 вопрос', validators=[DataRequired()])
    answer8 = StringField('Ответ на 8 вопрос', validators=[DataRequired()])
    answer9 = StringField('Ответ на 9 вопрос', validators=[DataRequired()])
    answer10 = StringField('Ответ на 10 вопрос', validators=[DataRequired()])
    submit = SubmitField('Увидеть результаты')


def oge_po_informatike(name, email):
    balls = 0
    sub_form = SubForm()
    with open("data/ОГЭ по информатике 1 задание.txt") as file1:
        task1 = file1.read()
    with open("data/ОГЭ по информатике 2 задание.txt") as file2:
        task2 = file2.read()
    with open("data/ОГЭ по информатике 3 задание.txt") as file3:
        task3 = file3.read()
    with open("data/ОГЭ по информатике 4 задание.txt") as file4:
        task4 = file4.read()
    with open("data/ОГЭ по информатике 5 задание.txt") as file5:
        task5 = file5.read()
    with open("data/ОГЭ по информатике 6 задание.txt") as file6:
        task6 = file6.read()
    with open("data/ОГЭ по информатике 7 задание.txt") as file7:
        task7 = file7.read()
    with open("data/ОГЭ по информатике 8 задание.txt") as file8:
        task8 = file8.read()
    with open("data/ОГЭ по информатике 9 задание.txt") as file9:
        task9 = file9.read()
    with open("data/ОГЭ по информатике 10 задание.txt") as file10:
        task10 = file10.read()
    with open("data/программа.txt") as prog:
        str1, str2, str3, str4, str5, str6 = map(str, prog.readlines())
    if sub_form.validate_on_submit():
        if sub_form.answer1.data == 'барс' or sub_form.answer1.data == 'Барс':
            balls += 1
        if sub_form.answer2.data == 'монгол' or sub_form.answer2.data == 'МОНГОЛ':
            balls += 1
        if sub_form.answer3.data == '32':
            balls += 1
        if sub_form.answer4.data == '10':
            balls += 1
        if sub_form.answer5.data == '6':
            balls += 1
        if sub_form.answer6.data == '4':
            balls += 1
        if sub_form.answer7.data == '7341256':
            balls += 1
        if sub_form.answer8.data == '111':
            balls += 1
        if sub_form.answer9.data == '27':
            balls += 1
        if sub_form.answer10.data == '25':
            balls += 1
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == email).first()
        reyt = user.reyting
        user.reyting = str(int(reyt) + balls)
        db_sess.commit()
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
                                    <h1>{name}, ваш результат за 1 часть ОГЭ: {balls} баллов!</h1>
                                    <p style="position:absolute;right:0;bottom:0;margin-bottom:0">
                                            <a href="/success">назад</a>
                                        </p>
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
                                    <h2>ОГЭ по информатике.</h2>
                                    <p>1)</p>
                                    {task1}<br>
                                    <p>2)</p>
                                    {task2}<br>
                                    <p>3)</p>
                                    {task3}<br>>
                                    <p>4)</p>
                                    {task4}<br>
                                    <p><img src="web_lyceum/data/tablica.jpg" alt="Таблица"></p>
                                    <p>5)</p>
                                    {task5}<br>
                                    <p>6)</p>
                                    {task6}<br>
                                    {str1}<br>
                                    {str2}<br>
                                    {str3}<br>
                                    {str4}<br>
                                    {str5}<br>
                                    {str6}<br>
                                    <p>7)</p>
                                    {task7}<br>
                                    <p><img src="web_lyceum/data/другая таблица.jpg" alt="Таблица"></p>
                                    <p>8)</p>
                                    {task8}<br>
                                    <p>9)</p>
                                    {task9}<br>
                                    <p><img src="web_lyceum/data/забыл как это называется.jpg" alt="Картинка"></p>
                                    <p>10)</p>
                                    {task10}<br>
                                    {render_template('login.html', form=sub_form)}
                                </body>
                            </html>"""
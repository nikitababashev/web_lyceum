#Сори, Никита, вчера уснул прям за столом. Так-что только сегодня отправляю.

from flask import Flask
from Task_creator import Create_Task

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def main():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Решалкин</title>
                      </head>
                      <body>
                        <h1>Тут пусто.</h1>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
def Create_Task(tyype, number, col_vo, txt, task, answers, link, ay=0):
    if tyype == 'main':
        return (f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Решалкин, задача №{number}</title>
                      </head>
                      <body>
                        <h1>Задача №{number}</h1>
                        <a href="http://127.0.0.1:8080/{link}/txt">Теория</a>.
                      </body>
                    </html>""",
                f"""<htnl lang="en">
                        <body>
                            <a href="http://127.0.0.1:8080/{link}/task{i}">Задание</a>.
                        </body>
                    </html>""" for i in range(col_vo))
    elif tyype == 'txt':
        with open(f"{txt}", mode="r") as txt:
            strs = txt.read()
        return f"""<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Решалкин, теория №{number}</title>
                        </head>
                        <body>
                            <h1>{strs}</h1>
                        </body>
                    </html>"""
    elif tyype == 'task':
        with open(f"{task}", mode="r") as task:
            strs = task.read()
        return f"""<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Решалкин №{number}, задача №{ay}</title>
                        </head>
                        <body>
                            <h1>{strs}</h1>
                            <form>
                                <div>
                                    <label for="answer">Введите ответ</label>
                                    <input type="text" id="answer" answer="answer"
                                     spellcheck="false" size="10">
                                </div>
                                <div>
                                    <button>Отправить</button>
                                </div>
                            </form>
                        </body>
                    </html>"""
from flask import Flask, url_for, redirect
import sqlite3

def index():
    conn = sqlite3.connect("Artistic.db")
    cursor = conn.cursor
    cursor.execute('SELECT name FROM artist WHERE "Birth Year" = (?)', [year])
    data = cursor.fetchall()

    if len(data) == 0:
        return "У базі немає двних не знайдено"
    elif len(data) == 1:
        return "У цьому році народився один художник"
    else:
        r = "<h3>Список художників</h3>"
        for person in data:
            r += person[0]
    return 

year = int(input("Введіть рік"))
app = Flask(__name__)
app.add_url_rule("/", "index", index)

if __name__ == "__main__":
    app.run()

from flask import Flask
counter = 0

def index():
   global counter
   counter = 0
   return '<a href="/counter">Далі</a>'

def counter():
   global counter
   counter = counter + 1
   return '<h1>' + str(counter) + '</h1>'

app = Flask(__name__)  

app.add_url_rule('/', 'index', index)                                   
app.add_url_rule('/counter', 'counter', counter)

if __name__ == "__main__":
   app.run()


from flask import Flask, render_template, request, flash, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'some_secret'
app.database = "sample.db"


@app.route('/', methods=['GET', 'POST'])
def home():
    with sqlite3.connect('sample.db') as g.db:
        error = None
        current = g.db.execute('select Name from posts')
        # print(current)
        names = [str(row[0]) for row in current.fetchall()]
        # print(names)
        if request.method == 'POST':
            name = request.form['username']
            if name in names:
                flash("hi there again {0}!".format(name))
            else:
                g.db.execute('INSERT INTO posts VALUES("{0}")'.format(name))
                flash("just hi {0}!".format(name))
        return render_template('home.html', error=error)


def connect_db():
    return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)

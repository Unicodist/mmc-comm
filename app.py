from db_models.configure_sqlalchemy import app
from flask import request, render_template


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/api/loginHandler', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    print(username)
    return "Hello There!"


if __name__ == "__main__":
    app.run(debug=True, port=8000)

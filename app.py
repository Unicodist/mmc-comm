from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/mmc-conn"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    uid = db.Column(db.Integer,primary=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.uid} - {self.name}"

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
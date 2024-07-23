from flask import Flask,session,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///contactos.sqlite'
app.config['SECRET_KEY']='5dfc118a7256f56d0fc1fcbef8759ccd'

db= SQLAlchemy(app)

# base de dato
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    email=db.Column(db.Text,nullable=False,unique=True)
    nombre=db.Column(db.Text,nullable=False)
    password=db.Column(db.Text,nullable=False)
    
class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    nombre=db.Column(db.Text,nullable=False)
    telefono=db.Column(db.Text,nullable=False)
    
with app.app_context():
    db.create_all()

# rutas seguras
@app.route("/update_contact/<id>")
def update_contact(id):
    pass

@app.route("/delete_contact/<id>")
def delete_contact(id):
    if session:
        obj=Contact.query.filter_by(id=id).first()
        db.session.delete(obj)
        db.session.commit()
    else:
        pass

# rutas no seguras
@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/login")
def login():
    session.clear()
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.clear()
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)
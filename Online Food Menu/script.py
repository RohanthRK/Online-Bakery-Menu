from flask import Flask,render_template ,request # importing Flask from flask library # will handle requests 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) # storing our application in app variable  (__name__ is the script.py)
ENV = 'dev'

if ENV =='dev':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Honeypot-Fermiparadox@localhost/bakery' # setting the connection to database
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #setting this to flase  to   avoid taking extra memoory
app.secret_key = 'secret string'# improves security

db = SQLAlchemy(app)


class Feedback(db.Model): # db.model is a relational model (uses table format)#determines the structure of data
    __tablename__ = 'feedback'
    id = db.Column(db.Integer,primary_key = True)
    brand = db.Column(db.String(200))
    quant = db.Column(db.Float)
    amount = db.Column(db.Float)

    def __init__(self,brand,quant,amount):
        self.brand = brand
        self.quant = quant
        self.amount = amount

class Feedback2(db.Model):
    __tablename__ = 'Cakes'
    id = db.Column(db.Integer,primary_key = True)
    flavour = db.Column(db.String(200))

    def __init__(self,flavour):
        self.flavour = flavour
class Feddback3(db.Model):
    __tablename__ = 'Pizza'

    id = db.Column(db.Integer,primary_key = True)
    crust = db.Column(db.Text)

    def __init__(self,crust):
        self.crust = crust




@app.route('/')# argument shlould be url , '/' indicates homepage
def home():
    return render_template('index.html')
@app.route('/burger')
def Burger():
    return render_template('bg.html')
@app.route('/pizza')
def Pizza():
    return render_template('pizza.html')
@app.route('/sandwich')
def Sandwich():
    return render_template('sandwich.html')
@app.route('/cake')
def Cake():
    return render_template('cake.html')
@app.route('/Drinks')
def Drinks():
    return render_template('Drinks (1).html')

@app.route('/submit',methods = ['POST'])
def submit():
    brand = request.form['brand']
    quant = request.form['quant']
    amount = request.form['amount']


    entry = Feedback(brand,quant,amount)
    db.session.add(entry)
    db.session.commit()
    return render_template('thankyu.html')
@app.route('/submit1',methods = ['POST'])
def submit1():
    flavour = request.form['flavour']


    entry1 = Feedback2(flavour) #creating an object
    db.session.add(entry1) # adding it to the session
    db.session.commit() # commiting the session
    return render_template('thankyu.html')

@app.route('/submit2',methods = ['POST'])
def submit2():

    crust = requests.form["crust"]

    entry2 = Feedback3(crust)
    db.session.add(entry2)
    db.session.commit()

    return render_template('thankyu.html')




if __name__ == '__main__': # name will be automatically assigned to main , # the conditions fails when the script is imported from else where
    db.create_all() # creates tables
    app.run() # running the application


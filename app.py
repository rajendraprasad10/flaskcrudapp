from flask import Flask,render_template, redirect, flash, request,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'Secrete_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/cruddata'
# for connecting with this database called mysqlphpadmin we must download this pip install Flask-MySQLdb for flask
app.config['SECRET_KEY'] = 'crud secrate'
db = SQLAlchemy(app)


#Creating formdata table for our cruddata database
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# this is the index page route
@app.route('/')
def index():
    # diplaying the data on the home page.
    all_data = FormData.query.all()
    return render_template('index.html', employees = all_data)



# this is reated to the insert data to database
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name  = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = FormData(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
        flash('Form Subminted Sucessfully!')
        return redirect(url_for('index'))


# this is route is used for update the database data
@app.route('/update', methods = ['GET', 'POST'])
def update():
    # getting the data from database.
    if request.method == 'POST':
        all_data = FormData.query.get(request.form.get('id'))
        all_data.name = request.form['name']
        all_data.email = request.form['email']
        all_data.phone = request.form['phone']
        db.session.commit()
        flash('your form was updated')
        return redirect(url_for('index'))

# this route id for delete the data from the list of employees
@app.route('/delete/<id>/', methods = ['POST', 'GET'])
def delete(id):
    my_data = FormData.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash('Employee Deleted sucessfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)




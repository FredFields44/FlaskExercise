

from ast import Num
from flask import Flask,redirect, render_template, url_for,request
from datetime import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
nbrs = []


@app.route('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.now()
    return render_template('index.html' , date = str(currentDate))


@app.route('/calculate', methods=['get','POST'])
def displayNumberPage():
    # Complete this function to display form.html page
    print(request.args)
    nbrs.append(request.form.get("num"))
    print(nbrs)
    return render_template('form.html')


@app.route('/calculation', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['num']

    return render_template('result.html' , nbrs = nbrs)


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    pass


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']

    # Append this value to studentOrganisationDetails

    # Display studentDetails.html with all students and organisations

if __name__ == "__main__":
    app.run()
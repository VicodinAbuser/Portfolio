from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/thank_you.html')
def thank_you():
    return render_template("thank_you.html")

def write_to_database(data):
    with open('database.txt', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}\n{subject}\n{message}\n')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods= ['POST','GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_database(data)
        write_to_csv(data)
        return redirect("/thank_you.html")
    else:
        return "Something went wrong. :( \nPlease try again. :)"


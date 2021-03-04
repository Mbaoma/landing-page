from app import app, render_template, request
from flask import render_template
import csv

def write_to_csv(data):
	with open('database.csv', mode='a') as database:
		email = data['email']
		csv_write = csv.writer(database, quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_write.writerow([email])

@app.route("/", methods={"POST", "GET"})
def index():
	if request.method == 'POST':
		email = request.form.get('email')
		write_to_csv(request.form)
		return render_template('thankyou.html')
	return render_template('index.html')
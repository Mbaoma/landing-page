from app import app
from flask import render_template, request
import csv

def write_to_csv(email: str):
	with open('database.csv', mode='a') as database:
		csv_write = csv.writer(database, quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_write.writerow(email)

@app.route("/", methods={"POST", "GET"})
def index():
	if request.method == 'POST':
		email = request.form.get('email')
		write_to_csv(email)
		return render_template('thankyou.html')
	return render_template('index.html')
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def map():
	return render_template('map.html')

app.run(debug=True)

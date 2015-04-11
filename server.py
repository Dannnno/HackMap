from flask import Flask, render_template, url_for


app = Flask(__name__, template_folder = ".")


@app.route('/')
def map():
	return render_template('example.html')

app.run(debug=True)

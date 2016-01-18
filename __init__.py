from __future__ import print_function
import os
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def homepage():
	viewer = 'clinician'
	description = 'This is the clinician version.'

	return render_template('index.html', viewer=viewer, description=description)

@app.route('/patient')
def patientpage():

	viewer = 'patient'
	description = 'This is the patient version.'

	return render_template('index.html', viewer=viewer, description=description)

@app.route('/echo/', methods=['GET'])
def echo():
    ret_data = {"value": request.args.get('echoValue')}
    return jsonify(ret_data)

@app.route('/about')
def aboutpage():

	viewer = 'about'
	return render_template('about.html', viewer=viewer)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True, use_reloader=True)
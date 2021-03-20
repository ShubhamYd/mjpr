import flask
from flask import request, jsonify
from flask_cors import CORS
import pickle
import os 
import numpy
dir_path = os.path.dirname(os.path.realpath(__file__))


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
# books = [
#     {'id': 0,
#      'title': 'A Fire Upon the Deep',
#      'author': 'Vernor Vinge',
#      'first_sentence': 'The coldsleep itself was dreamless.',
#      'year_published': '1992'},
#     {'id': 1,
#      'title': 'The Ones Who Walk Away From Omelas',
#      'author': 'Ursula K. Le Guin',
#      'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
#      'published': '1973'},
#     {'id': 2,
#      'title': 'Dhalgren',
#      'author': 'Samuel R. Delany',
#      'first_sentence': 'to wound the autumnal city.',
#      'published': '1975'}
# ]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>ML API</h1>
<p>An api for Stock Market Analysis using Arima, LSTM and Prophet</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/arima', methods=['GET'])
def api_arima():
	b = []
	print(request.args.get("filename"))
	print(type(request.args.get("filename")))
	filename = str(request.args.get("filename"))

	with open(f'server-output/arima/{filename}/{filename}-arima.pickle', 'rb') as handle:
		b = pickle.load(handle)
	return jsonify(b)
# http://127.0.0.1:5000/api/arima?filename=apple

@app.route('/api/lstm', methods=['GET'])
def api_lstm():
	b = []
	print(request.args.get("filename"))
	print(type(request.args.get("filename")))
	filename = str(request.args.get("filename"))

	with open(f'server-output/lstm/{filename}/{filename}-lstm.pickle', 'rb') as handle:
		b = pickle.load(handle)
	return jsonify(b)

#create api for news title

app.run()
# http://127.0.0.1:5000/api/lstm?filename=apple

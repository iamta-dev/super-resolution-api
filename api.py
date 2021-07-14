import warnings
warnings.filterwarnings("ignore")

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#------------------------------

from flask import Flask, jsonify, request, make_response
from resolution import super_resolution


import argparse
import uuid
import json
import time
from tqdm import tqdm

#------------------------------

from flask_cors import CORS

#------------------------------

app = Flask(__name__)

#------------------------------
# 'Access-Control-Allow-Origin' header
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#------------------------------
#Service API Interface
@app.route('/superResolution', methods=['POST'])
def superResolution():

	req = request.get_json()

	#---------------------------

	raw_content = []
	if "img" in list(req.keys()):
		raw_content = req["img"]

	#---------------------------

	img_req = super_resolution(raw_content[0])




	# toc = time.time()
	resp_obj = jsonify({
		'img': img_req
		})

	return resp_obj, 200

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'-p', '--port',
		type=int,
		default=5500,
		help='Port of serving api')
	args = parser.parse_args()
	app.run(host='0.0.0.0', port=args.port)

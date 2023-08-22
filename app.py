from flask import Flask, request, send_file
import time
import os


if not os.path.isdir('images'):
	os.mkdir('images')


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
	return "cdn is live; CRUD system:\n<code><pre>" \
		   "POST:   /create         - upload photo (input: file 'photo', output: file id);\n" \
		   "GET:    /{file id}.png  - read   photo\n" \
		   "PUT:    /{file id}      - update photo (input: new photo file)\n" \
		   "DELETE: /{file id}      - delete photo </pre></code>"

@app.route('/<int:id>', methods=['GET'])
def handle_get(id):
	return send_file(f'images/{id}.png')


@app.route('/create', methods=['POST'])
def handle_post():
	file_id = int(time.time())
	file = request.files['photo']
	file_content = file.read()

	with open(f'images/{file_id}.png', 'wb') as output:
		output.write(file_content)

	return {'id': file_id}


@app.route('/<int:id>', methods=['UPDATE'])
def handle_update(id):
	try:
		file = request.files['photo']
		file_content = file.read()
		with open(f'images/{id}', 'wb') as output:
			output.write(file_content)

		return {'status': 'sucessfully update photo'}, 202

	except Exception as e:
		return {'status': 'aborted', 'details': e}, 400


@app.route('/<int:id>', methods=['DELETE'])
def handle_delete(id):
	try:
		os.remove(f'images/{id}')

		return {'status': 'sucessfully delete photo'}, 202
	
	except FileNotFoundException:
		return {'status': 'not found'}, 404


app.run(port=5202)
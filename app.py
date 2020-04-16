from quart import (
    abort, jsonify, make_push_promise, Quart, render_template, request, url_for,
)
import hashlib
import json

app = Quart(__name__)


@app.route('/')
async def index():
    await make_push_promise(url_for('static', filename='style.css'))
    await make_push_promise(url_for('static', filename='script.js'))
    await make_push_promise(url_for('static', filename='assets/images/body-image/icon-96x96.png'))
    await make_push_promise(url_for('static', filename='assets/images/body-image/icon-192x192.png'))
    return await render_template('index.html')

@app.route('/', methods=['POST'])
async def get_response():
    response = await request.get_json()
    response_data = response['inputstring']
    _encoded_block = json.dumps(response_data, sort_keys = True).encode()
    _encoded_block_hash = hashlib.sha256(_encoded_block).hexdigest()
    return jsonify(_encoded_block_hash)

@app.cli.command('run')
def run():
    app.run(port=5000, debug=True, keyfile='key.pem', certfile='cert.pem')


if __name__ == "__main__":
    run()
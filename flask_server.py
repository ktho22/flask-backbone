import argparse
import time
import os
from os.path import join
from flask import Flask, jsonify, request, Response, make_response, send_file

bb = time.time()
app = Flask(__name__)
parser = argparse.ArgumentParser(description='Flask server scrpit')

# data load
parser.add_argument('--port', type=int, default=8081, help='port number for api')
args = parser.parse_args()


@app.route('/', methods=['POST'])
def calc():
    print('request.form : {}'.format(request.form))
    sentence = request.form['sentence'] if 'sentence' in request.form.keys() else None
    
    save_path = './M1.4/'
    os.makedirs(save_path, exist_ok=True)
    with open(join(save_path, 'SAVETO.txt'), 'w') as f:
        f.write(sentence)
    print(sentence)
    return 'success'

if __name__ == '__main__':
    print('pre-loading takes {}s'.format(time.time() - bb))
    app.run(host='0.0.0.0', port=args.port)

import sys

import vscores

from flask import Flask, jsonify, make_response, abort

__API_URL_BASE = '/api/beta/'

__config_file = sys.argv[1]
app = Flask(__name__)


@app.route('{0}scores'.format(__API_URL_BASE), methods=['GET'])
def get_coins():
    return jsonify(vscores.vespucci_scores(__config_file))


@app.route('{0}scores/<string:coin_id>'.format(__API_URL_BASE), methods=['GET'])
def get_coin_by_id(coin_id):
    coin_history = vscores.vespucci_coin_scores(__config_file, coin_id)
    if len(coin_history) == 0:
        abort(404)
    return jsonify(coin_history)


@app.route('{0}scores/list'.format(__API_URL_BASE), methods=['GET'])
def get_coins_list():
    coins_list = vscores.vespucci_scores_coins_list(__config_file)
    return jsonify(coins_list)


@app.route('{0}coins'.format(__API_URL_BASE), methods=['GET'])
def get_vespucci_coins():
    coins_list = vscores.vespucci_coins(__config_file)
    return jsonify(coins_list)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 80)


import logging
import time
import sys

from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # Add this line
handler.setLevel(logging.INFO)  # Set the level for the handler
logger.addHandler(handler)  # Add the handler to the logger

app = Flask(__name__)
metrics = PrometheusMetrics(app)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


@app.route('/wait-n', methods=['GET'])
def wait_n():
    n = request.args.get('n', type=int)
    logger.info(f'Received request for /wait-n: {n}')
    if n is None:
        logger.error("Request for /wait-n failed: n is not an integer.")
        return jsonify({"error": "Please provide an integer as n."}), 400
    time.sleep(n)
    logger.info(f"Waited for {n} seconds as requested.")
    return jsonify({"message": "Waited for {} seconds".format(n)})


@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    global successful_requests

    n = request.args.get('n', type=int)

    if n is None:
        return jsonify({"error": "Please provide an integer asdf n."}), 400

    result = fibonacci(n)
    return jsonify({"fibonacci": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True, debug=True, threaded=False)

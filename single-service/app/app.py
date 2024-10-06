from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

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

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    global successful_requests

    n = request.args.get('n', type=int)

    if n is None:
        return jsonify({"error": "Please provide an integer asdf n."}), 400

    result = fibonacci(n)
    return jsonify({"fibonacci": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

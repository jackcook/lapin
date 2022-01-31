from flask import Flask, g, jsonify, send_file
import time
import numpy as np

import logging
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)

latencies = []

@app.route("/")
def index():
    return send_file("dog.jpg")

@app.route("/tail_latency")
def tail_latency():
    percentiles = [50, 90, 99, 99.9]

    return jsonify({
        # "latencies": latencies,
        "num_requests": len(latencies),
        "percentiles": {
            p: float("{:.2f}".format(np.percentile(latencies, p) * 1000)) if len(latencies) > 0 else 0 for p in percentiles
        }
    })

@app.before_request
def before_request():
    g.start = time.time()

@app.after_request
def after_request(response):
    diff = time.time() - g.start
    print(diff)
    latencies.append(diff)
    return response

app.run(host="0.0.0.0", port=8080, threaded=True)
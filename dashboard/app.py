"""
==========================================
Nova Mission Control API
Nova-Trader-BM
==========================================
"""

from flask import Flask, jsonify

from dashboard.data import DashboardData


app = Flask(__name__)

data = DashboardData()


@app.route("/")

def home():

    return """

    <h1>Nova Mission Control</h1>

    <p>System Online</p>

    """


@app.route("/status")

def status():

    return jsonify(

        data.get_status()

    )


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000

    )

"""
==========================================
Nova Mission Control
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

<!DOCTYPE html>

<html>

<head>

<title>
Nova Mission Control
</title>


<link rel="stylesheet" href="/static/style.css">


</head>


<body>


<div class="title">

NOVA MISSION CONTROL

</div>



<div class="card">

<div class="header">
SYSTEM STATUS
</div>


<p>
Bot:
<span id="bot">
ONLINE
</span>
</p>


<p>
Brain:
<span id="brain">
ACTIVE
</span>
</p>


</div>



<div class="card">

<div class="header">
CONFIDENCE ENGINE
</div>


<div class="value">

<span id="confidence">
94
</span>%

</div>


</div>



<div class="card">

<div class="header">
ACCOUNT PERFORMANCE
</div>


<p>
Trades Today:

<span id="trades">
0
</span>

</p>


<p>
Profit:

<span id="profit">
0
</span>

</p>


</div>



<div class="card">

<div class="header">
NOVA BRAIN ANALYSIS
</div>


<ul>

<li>
Trend: Bullish
</li>


<li>
Momentum: Strong
</li>


<li>
Risk: Acceptable
</li>


<li>
Setup Match: 78%
</li>


</ul>


</div>



<div class="card">

<div class="header">
MARKET RADAR
</div>


<p>
EURUSD 🟢
</p>


<p>
GBPUSD 🟡
</p>


<p>
XAUUSD 🔴
</p>


</div>


<script src="/static/dashboard.js"></script>



</body>

</html>

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

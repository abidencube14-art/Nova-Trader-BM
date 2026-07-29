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
<span class="online">
ONLINE
</span>
</p>


<p>
Brain:
ACTIVE
</p>


<p>
Learning Engine:
ACTIVE
</p>


</div>



<div class="card">

<div class="header">
TRADING TELEMETRY
</div>


<p>
Confidence:

<span class="value">
94%
</span>

</p>


<p>
Risk:
0.75%

</p>


<p>
Trades Today:
0

</p>


</div>



<div class="card">

<div class="header">
ACCOUNT PERFORMANCE
</div>


<p>
Win Rate:
0%

</p>


<p>
Profit:
0

</p>


</div>



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

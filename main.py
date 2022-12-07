from flask import Flask, render_template, url_for, request
from simplex import simplex

app = Flask(__name__)

@app.route('/simplex')
def http_simplex():

    print(request)

    prbl = {
        # 'variaveis': 2,
        # 'tipo': float,
        'minimizar': False,
        'objetivo': '1*x1 + 1*x2',
        'restricoes': [
            '24*x1 + 16*x2 <= 96',
            '500*x1 + 1000*x2 <= 4500'
        ],
        'restricoesVars': [
            'x1 >= 0',
            'x2 >= 0'
        ]
    }

    headers = {
        'Content-Type': 'application/json'
    }

    return simplex(prbl), 200, headers


if __name__ == "__main__":
    app.run(debug=True)
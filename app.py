from flask import Flask, render_template, jsonify, make_response, json

app = Flask(__name__)

#main
@app.route('/')
def main():
    return render_template("index.html")


#/generar/leidsa/lotto
@app.route('/generar/leidsa/lotto')
def generar_lotto():
    return render_template("lotto.html")


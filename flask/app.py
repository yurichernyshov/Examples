from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/app")
def index():
    return "Hello!" 

if __name__=="__main__":
    app.run('0.0.0.0', 9999, debug=True)


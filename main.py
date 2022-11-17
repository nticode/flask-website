from flask import Flask, render_template
app = Flask(__name__)
item = "LED"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/api/<state>", methods = ['POST'])
def on(state):
    # {state} can be "on" or "off"
    print(state)

    return {"message": f"{item} has been turned {state}"}

app.run('127.0.0.1', '1011', debug=True)
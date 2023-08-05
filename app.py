from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # the '@' is a decorater
def hello_world(): # define a function named hello_world
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
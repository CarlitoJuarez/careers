from flask import Flask

app = Flask(__name__)

@app.route("/") # the '@' is a decorater
def hello_world(): # define a function named hello_world
    return 'hello'
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/Hola")
def hola():
    return "Hola mundooo"

if __name__=="__main__":
    app.run(debug=True,port=3000)


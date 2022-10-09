from flask import Flask 
app = Flask(__name__) 

@app.route('/')         
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<random>')
def random(random):
    return f"Hi {random.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word*num}"

if __name__=="__main__":  
    app.run(debug=True)    


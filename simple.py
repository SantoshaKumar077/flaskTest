# This is progaram to show a static introductory web page using Flask.

from flask import Flask
app = Flask(__name__)

@app.route('/')     #App routing is used to map the specific URL with the associated function that is intended to perform some task.
def hello():
    return "<h1><i>Hello World!</i></h1>"       # This indicates that we can use html formatting with flask.
@app.route('/test')
def func():
    return "Welcome to flask tutorials!"
@app.route('/name/<name>')      # Here whatever name a user passes in the url (eg: localhost/name/example), it is passed into the function parameter "name"
def name(name):
    return f"<h1>Hey! Hii {name}. Welcome to Flask tutorial</h1>"
@app.route('/name/')    # I f no name is passed, then return hii there.
def emptyname():
    return "<h1>Hii there. Welcome to flask tutorial</h1>"
@app.route('/name/<name>/<int:age>')
def agenname(name,age):
    return "Hey %s! Now you are %d years old.</h1>" %(name,age);
if __name__== "__main__":
    app.run(debug=True, host="127.1.0.7", port=8085)
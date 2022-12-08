# Progarm to show how to use render_template function of Flask.

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")    #this will parse the content from index.html and show here.
@app.route('/about')
def about():
    var=render_template(["about.html"])   #the result of render function has been stored in a var and render template() can take value as a list.
    return var    #this will parse the content from about.html and show here.
    
if __name__== "__main__":
    app.run(debug=True)
    print("hello world")    #this indicates that print() function is not returning an output to console when we use flask  
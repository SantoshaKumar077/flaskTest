## This program shows how to use different HTTP methods in flask. And how can we get values from a html file.

from flask import *
app=Flask(__name__)

@app.route('/user')
def user():
    return render_template('forms.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        username=request.args.get('username')       # shows that request.args function is used for Get method to avoid BadRequestKeyError.
        password=request.args.get('password')
        if username=="santosh" and password=="kumarPass":  
            return "Welcome %s" %username
        else:
            return "Hey %s! Your password is %s." %(username,  password);
    if request.method == "POST":
        username=request.form.get('username')       # shows that request.form is used for post method.
        password=request.form.get('password')
        if username=="ayush" and password=="google":  
            return "Welcome %s" %username
        else:
            return "Hey %s! Your password is %s. Please save it." %(username,  password);
if __name__ == '__main__':  
   app.run(debug = True)  
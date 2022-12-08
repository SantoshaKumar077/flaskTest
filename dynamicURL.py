## This is method used for dynamic url routing.

from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return '<h1>Hey admin ! U have no notification yet.</h1>'  
  
@app.route('/librarion')  
def librarion():  
    return '<h1>Hey librarion! There is no pending work in the pipeline.</h1>'  
  
@app.route('/student')  
def student():  
    return '<h1>Hey student! Please return the books in time.</h1>'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))
    if name == 'librarion':  
        return redirect(url_for('librarion'))
    if name == 'student':  
        return redirect(url_for('student'))
if __name__ =='__main__':  
    app.run(debug = True)
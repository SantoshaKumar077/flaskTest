## This program describes how to get data from a html form and use those values in another html file.

from flask import *  
app = Flask(__name__)  
  
@app.route('/')  
def customer():  
   return render_template('customerForm.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  ## Here result is the dictionary containing all the values provided in the form.
      return render_template("resultForm.html",result = result)  
   
if __name__ == '__main__':  
   app.run(debug = True) 
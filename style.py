## This shows how to use stylesheets with flask.

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('style.html')  
if __name__ == '__main__':  
   app.run(debug = True)  
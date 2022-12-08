from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import logging
UPLOAD_FOLDER="C:\\Users\\SantoshaKumar\\ProjectWork\\flask"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   return render_template('files.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      logging.warning(f)
      logging.warning(filename)
      return render_template("hello.html")
		
if __name__ == '__main__':
   app.run(debug = True)
   
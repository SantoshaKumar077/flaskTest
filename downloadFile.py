from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('downloadFile.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def download():
   if request.method == 'GET':
      return send_from_directory(directory="flask\\templates\\about.html", path="copiedFile.html")
		
if __name__ == '__main__':
   app.run(debug = True)
   
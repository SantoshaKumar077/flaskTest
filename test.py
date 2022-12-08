## This is to show how conditional forms can be achieved using jinja templates.

from flask import *
import logging

app = Flask(__name__)

# @app.route("/condition")
# def condForm():
#     if request.method=="POST":
#         global svcType
#         svcType=request.form.get('svcType')
#         render_template('test.html', svcType=svcType)
@app.route("/test", methods=["GET","POST"])
def showForm():
    return render_template('test.html')





if __name__ == "__main__":
    app.run(debug=True)

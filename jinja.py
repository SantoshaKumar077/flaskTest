## This program shows how to use jinja templates and its corresponding delimiteres to alllow dyanamic data representation.


from flask import *
app = Flask(__name__)


@app.route('/table/<int:num>')
def table(num):
    return render_template('jinja.html', numTable=num)

if __name__ == "__main__":
    app.run(debug=True)

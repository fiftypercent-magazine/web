from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/about.html")
def about():
    return render_template('about.html')


#TODO make 404html redirect to main.
@app.errorhandler(404)
def page_not_found_error(error):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import render_template
from models import Page 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/issue<issue_no>.html')
def page(issue_no):
    context = Page(issue_no).getContext()
    context['title'] = 'FiftyPercent - No.' + issue_no
    # toggler icon
    return render_template('page.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)

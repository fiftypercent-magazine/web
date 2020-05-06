from flask_frozen import Freezer, url_for
from app import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.run(debug=True)

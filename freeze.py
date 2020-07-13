from flask_frozen import Freezer
from app import app

from models import Page

freezer = Freezer(app)

FREEZER_RELATIVE_URLS = True

@freezer.register_generator
def page():
    issues = Page().all()
    for issue in range(1, issues):
        yield {'issue_no': issue}

if __name__ == '__main__':
    freezer.freeze()

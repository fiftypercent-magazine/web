import json

DATA_JSON = 'static/media/page_link.json'
#DATA_JSON = 'static/media/page_link_dev.json'

class Page:
    def __init__(self, issue_no=1):
        self.issue = issue_no 

    def __repr__(self):
        return 'fp_{}'.format(self.issue)

    def getContext(self):
        data = self.loadData()
        try:
            context = data[self.issue]
        except KeyError:
            context = {'issue_not_found': 'url_not_found'}
        return context

    def all(self):
        data = self.loadData()
        return len(data)

    def loadData(self):
        with open(DATA_JSON, 'r') as data_json:
            data = json.load(data_json)
        return data

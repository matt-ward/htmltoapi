import os.path as path
import uuid


class Builder:

    def __init__(self, config):
        self.config = config

    def create(self):

        f = open(path.abspath(path.join(__file__,"../../server/apiserver.py")), 'wa')

        f.write("""
import json
from htmltoapi import pagerequester
from htmltoapi import pageparser
from flask import Flask
app = Flask(__name__)

        """)

        for resource in self.config['resources']:

            f.write("""
@app.route("/api/"""+resource['name'].lower()+"""s")
def z"""+str(uuid.uuid4()).replace('-', '')+"""():
    config = """+str(resource)+"""
    page = pagerequester.Requester(\""""+resource['source_url']+"""\").fetch_page_as_text()
    parser = pageparser.Parser(config, page)
    data = parser.parse()
    return json.dumps(data)

if __name__ == '__main__':
    app.run()

            """)

        f.close()

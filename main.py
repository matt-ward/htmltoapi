from htmltoapi import pageparser
from htmltoapi import pagerequester


config = {

    "elements": [
        {
            "name": "link",
            "element": {
                "type": "a",
                "class": "hgpm-link",
                "attribute": "href"
            }
        },
        {
            "name": "title",
            "element": {
                "type": "p",
                "class": "hgpm-image-hed"
            }
        }

    ]}


page = pagerequester.Requester("http://www.burlingtonfreepress.com/news/local/").fetch_page_as_text()
parser = pageparser.Parser(config, page)
data = parser.parse()

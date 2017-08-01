import requests
from requests import RequestException
import json
import logging
from bs4 import BeautifulSoup
import traceback

logging.basicConfig()
logger = logging.getLogger('pagerequester')


class Requester:

    def __init__(self, url):

        self.url = url
        self.options = {}

    def configure(self, **opts):

        self.options = opts

    def fetch_page_as_text(self):
        return requests.get(self.url).text

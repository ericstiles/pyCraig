#!/usr/bin/python
import re
import requests as req
from bs4 import BeautifulSoup as bs

image_url_prepend = 'https://images.craigslist.org/'
image_url_append = '_300x300.jpg'


def get_html_page_text(url: str) -> str:
    """
    not a function.
    given a url return the text of that page

    need to wrap in try/except to check for status and return
    an empty page if an error happened

    :param url:
    :return:
    """
    return req.get(url).text


def get_souped_up_text(text) -> bs:
    """

    :rtype: bs
    """
    return bs(text, 'html.parser')
    # return bs(text, 'lxml')


def get_image_urls(data_ids: str, prepend: str, append: str) -> list:
    return list(map(lambda x: f"{prepend}{x}{append}", re.compile('.?:([A-Za-z0-9_]+),').findall(data_ids)))

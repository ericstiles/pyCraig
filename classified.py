from __future__ import annotations
from bs4 import Tag
import utils as u
import re


class Advertisement:
    def __init__(self, id: str, title: str, link: str, price: str, year: str, image_list: list):
        self.id = id
        self.title = title
        self.link = link
        self.price = price
        self.image_list = image_list
        self.year = year

    def __str__(self):
        return self.id + ", " + self.title + ", " + self.price + ", " + self.link + ", " + str(self.image_list)

    def __repr__(self):
        return self.__str__()

    def hash(self):
        return self.title + ", " + self.price + ", " + str(len(self.image_list))

    @staticmethod
    def map_li_to_model(tag: Tag) -> Advertisement:
        a = tag.find('a')
        if hasattr(a.find('span'), 'text'):
            price = a.find('span').text
        else:
            price = 'UNKNOWN PRICE'
        link = a['href']
        data_ids_list = []
        if 'data-ids' in a.attrs:
            data_ids_list.extend(
                u.get_image_urls(a['data-ids'], prepend=u.image_url_prepend, append=u.image_url_append))
        title_tag = tag.find('a', {'class': 'result-title hdrlnk'})
        title = title_tag.text
        id = title_tag.attrs['data-id']
        r = re.search("\\d{4}", title)
        year = r.group(0) if r else ""
        return Advertisement(id, title, link, price, year, data_ids_list)

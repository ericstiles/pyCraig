import utils as u
from bs4 import BeautifulSoup as bs

base_url = 'https://www.craigslist.org/about/sites'


def get_all_sites_dict(soup: bs) -> dict:
    """
    given specific craigslist url get all states in a dictionary.

    Could be written to be more functional

   :rtype: dict
   """
    a = soup.find('div', {"class": "colmask"}).find_all('a')
    d = dict()
    for i in a:
        d[i.getText()] = i['href']
    return d


def get_sites_by_state_dict(soup: bs) -> dict:
    """

    :param soup:
    :return:
    """
    pass


def handle(sites_base_url: str) -> dict:
    page = u.get_html_page_text(sites_base_url)
    soup = u.get_souped_up_text(page)
    href_listing = get_all_sites_dict(soup)
    return href_listing

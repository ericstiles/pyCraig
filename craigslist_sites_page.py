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
    a = soup.find('a', {"name": "US"}).parent.find_all_next('h4')
    num = 1
    d = {}
    for i in a:
        d[i.getText()] = []
        num = num + 1

        b = i.find_next('ul')
        for j in b.find_all('a'):
            d[i.getText()].append({j.getText(): j['href']})

        if (num == 52):
            break
    return d

def handle_sites_by_state(sites_base_url: str) -> dict:
    page = u.get_html_page_text(sites_base_url)
    soup = u.get_souped_up_text(page)
    return get_sites_by_state_dict(soup)


def handle(sites_base_url: str) -> dict:
    page = u.get_html_page_text(sites_base_url)
    soup = u.get_souped_up_text(page)
    href_listing = get_all_sites_dict(soup)
    return href_listing

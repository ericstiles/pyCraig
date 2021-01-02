#!/usr/bin/env python
"""
Module Docstring
"""
import argparse
import craigslist_search_results_page as results_page
import craigslist_sites_page as sites_page
import search_criteria as sc
import utils as u
import console as c

__author__ = "Eric Stiles"
__version__ = "0.1.0"
__license__ = "MIT"


def map_url_to_results(url: str, search_string: str, search: str) -> list:
    text = u.get_html_page_text(results_page.get_search_query(url, search_string, search))
    inner_results_list = map_page_to_results(text)
    return results_page.reduce_page_results(inner_results_list)


def map_page_to_results(page: str) -> list:
    soup = u.get_souped_up_text(page)
    inner_results_list = soup.find_all(results_page.tag_filter)
    return results_page.reduce_page_results(inner_results_list)


def main(args: argparse.Namespace):
    """ Main entry point of the app """
    dict_sites = sites_page.handle(sites_page.base_url)

    bridge = []
    if type(args.subdomain) == str:
        bridge.append(args.subdomain)
    else:
        bridge.extend(args.subdomain)

    for site in bridge:
        # print(dict_sites[site])
        site = dict_sites[site]
        # print(results_page.get_search_query(site, sc.car_search_path, args.data[0]))
        results_list = map_url_to_results(site, sc.car_search_path, args.data[0])
        c.handle(results_list)


def parse() -> argparse.Namespace:
    default_search_domain = 'san antonio'

    parser = argparse.ArgumentParser(description='Craigslist search.')
    parser.add_argument("-o", "--output", help="output the results to the console")
    parser.add_argument("-s", "--subdomain", help='subdomains to search', nargs='+', default=default_search_domain)
    parser.add_argument("-d", "--data", help='search values', nargs=1, default=default_search_domain, required=True)
    # print(parser.parse_args())
    return parser.parse_args()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(parse())

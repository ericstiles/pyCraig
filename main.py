#!/usr/bin/env python
"""
Module Docstring
"""
import argparse
from typing import List, Any, Callable, Union

import craigslist_search_results_page as results_page
import craigslist_sites_page as sites_page
import search_criteria as sc
import utils as u
from output import Output as o
from output import Html as H
from output import ConsoleOutput
from classified import Advertisement

__author__ = "Eric Stiles"
__version__ = "0.1.0"
__license__ = "MIT"

process_parser_args: Callable[[Any], Union[List[Any], Any]] = \
    lambda arg: [] + [arg] if type(arg) == str else [] + arg


def map_url_to_results(url: str, search_string: str, arg: {}) -> list:

    query_parameter=""
    if arg.data:
        query_parameter=query_parameter + "query=" + arg.data[0] + "&"
    if arg.max:
        query_parameter=query_parameter + "max_auto_year=" + arg.max[0] + "&"
    if arg.min:
        query_parameter=query_parameter + "min_auto_year=" + arg.min[0] + "&"

    text = u.get_html_page_text(results_page.get_search_query(url, search_string, query_parameter))
    inner_results_list = map_page_to_results(text)
    return results_page.reduce_page_results(inner_results_list)


def map_page_to_results(page: str) -> list:
    soup = u.get_souped_up_text(page)
    inner_results_list = soup.find_all(results_page.tag_filter)
    return results_page.reduce_page_results(inner_results_list)


def main(args: argparse.Namespace):
    """ Main entry point of the app """
    dict_sites = sites_page.handle(sites_page.base_url)
    dict_outputs = {'console': ConsoleOutput(), 'html': H()}

    results_list=[]
    search_list = [site for site in args.subdomain]
    if len(search_list) == 0:
        search_list = dict_sites;
    for site in search_list:
        site = dict_sites[site.replace("_", " ")]
        results_list = results_list + list(map(lambda i: Advertisement.map_li_to_model(i),
                                               map_url_to_results(site, sc.car_search_path,
                                                                  args)))
    results_list = u.reduce(results_list);
    print (dict_outputs[process_parser_args(args.output)[0]].handle(results_list))


def parse() -> argparse.Namespace:
    """
    Parse command line arguments
    :return:  argparse.Namespace
    """
    # default_search_domain = ['san antonio']
    default_search_domain = []
    default_output = 'console'

    parser = argparse.ArgumentParser(description='Craigslist search.')
    parser.add_argument("-o", "--output", help="output the results to the console", nargs=1, default=default_output)
    parser.add_argument("-s", "--subdomain", help='subdomains to search', nargs='+', default=default_search_domain)
    parser.add_argument("-d", "--data", help='search values', nargs=1, default=default_search_domain, required=True)
    parser.add_argument("-a", "--max", help='max year', nargs=1, required=False)
    parser.add_argument("-i", "--min", help='min year', nargs=1, required=False)
    return parser.parse_args()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main(parse())

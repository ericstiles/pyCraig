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

import sys

__author__ = "Eric Stiles"
__version__ = "0.1.0"
__license__ = "MIT"

def list_domains_by_state(args: argparse.Namespace):
    dict_sites = sites_page.handle_sites_by_state(sites_page.base_url)
    for i in dict_sites[args.state]:
        print (i)

def list_domains(args: argparse.Namespace):
    dict_sites = sites_page.handle(sites_page.base_url)
    for site in dict_sites:
        # Could be a a list of words to check
        if (args.filter is not None and args.filter[0] in site) or args.filter is None:
            print (site + " : " + dict_sites[site.replace("_", " ")])

def search(args: argparse.Namespace):
    dict_sites = sites_page.handle(sites_page.base_url)
    dict_outputs = {'console': ConsoleOutput(), 'html': H()}

    results_list=[]
    search_list = [site for site in args.subdomain]
    if args.state is not None:
        state_dict_sites = sites_page.handle_sites_by_state(sites_page.base_url)
        for i in args.state:
            for j in state_dict_sites[i]:
                search_list.extend(j.keys())

    if len(search_list) == 0:
        search_list = dict_sites;
    for site in set(search_list):
        site = dict_sites[site.replace("_", " ")]
        results_list = results_list + list(map(lambda i: Advertisement.map_li_to_model(i),
                                               map_url_to_results(site, sc.search[args.category[0]],
                                                                  args)))
    results_list = u.reduce(results_list);
    print (dict_outputs[process_parser_args(args.output)[0]].handle(results_list))


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

def process():
    """
    Parse command line arguments
    :return:  argparse.Namespace
    """
    default_search_domain = []
    default_output = 'console'

    parser = argparse.ArgumentParser(description='Craigslist search')

    sub_parsers = parser.add_subparsers(help='sub-commmand help')

    parser_list = sub_parsers.add_parser('list', help='list subdomains')
    parser_list.add_argument("-f", "--filter", help='filter sites in list', nargs=1)
    parser_list.set_defaults(func=list_domains)

    parser_list_state = sub_parsers.add_parser('list-state', help='list sub domains by state')
    parser_list_state.add_argument("-t", "--state", help='state to show (required)', nargs=1)
    parser_list_state.set_defaults(func=list_domains_by_state)

    parser_search = sub_parsers.add_parser('search', help='search for products')
    parser_search.add_argument("-o", "--output", help="output the results to the console [output, html]", nargs=1, default=default_output)
    parser_search.add_argument("-s", "--subdomain", help='subdomains to search', nargs='+', default=default_search_domain)
    parser_search.add_argument("-t", "--state", help='state subdomains', nargs='+')
    parser_search.add_argument("-d", "--data", help='search values', nargs=1, default=default_search_domain, required=True)
    parser_search.add_argument("-a", "--max", help='max year, specific to car search', nargs=1, required=False)
    parser_search.add_argument("-i", "--min", help='min year, specific to car search', nargs=1, required=False)
    parser_search.add_argument("-c", "--category", help='category to search in [cars, electronics, motorcycles, tools]', nargs=1, required=False)
    parser_search.set_defaults(func=search)

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args =  parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    process()

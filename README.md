# main

There are no core arguments

```
$ main.py

usage: main.py [-h] {list,search} ...

Craigslist search

positional arguments:
{list,search}  sub-commmand help
list         list the sub-domains searched in craigslist
search       search sub-domains given the relevant search criteria

optional arguments:
-h, --help     show this help message and exit
```

#list

The generated list of all sub-domains based on sites in the craigslist [`about/sites` ](https://www.craigslist.org/about/sites) page.

```
$ main.py list -h
usage: main.py list [-h] [-f FILTER]

optional arguments:
  -h, --help            show this help message and exit
  -f FILTER, --filter FILTER
                        filter sites in list by confirming if filter string is a substring
```

Example of list command
```
$ ./main.py list

auburn : https://auburn.craigslist.org/
birmingham : https://bham.craigslist.org/
dothan : https://dothan.craigslist.org/
florence / muscle shoals : https://shoals.craigslist.org/
...
```

##filter

The filter will check the text of the url link in the `about/sites` page to find a specific domain. This sub-command and filter helps to determine which sub-domains to use for two word or slash combinations.

Example 1
```
$ ./main.py list -f dallas

dallas / fort worth : https://dallas.craigslist.org/
```

Example 2
```
$ ./main.py list -f fort

fort smith : https://fortsmith.craigslist.org/
fort collins / north CO : https://fortcollins.craigslist.org/
fort lauderdale : https://miami.craigslist.org/
fort wayne : https://fortwayne.craigslist.org/
fort dodge : https://fortdodge.craigslist.org/
dallas / fort worth : https://dallas.craigslist.org/
```

#search

Search across all or a given set of sub-domains in a specific search category

```aidl
$ ./main.py search -h
usage: main.py search [-h] [-o OUTPUT] [-s SUBDOMAIN [SUBDOMAIN ...]] -d DATA [-a MAX] [-i MIN] [-c CATEGORY] [-l LIST]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output the results to the console [output, html]
  -s SUBDOMAIN [SUBDOMAIN ...], --subdomain SUBDOMAIN [SUBDOMAIN ...]
                        subdomains to search
  -d DATA, --data DATA  search values
  -a MAX, --max MAX     max year, specific to car search
  -i MIN, --min MIN     min year, specific to car search
  -c CATEGORY, --category CATEGORY
                        category to search in [cars, electronics, motorcycles, tools]

```

#example request to match
```
https://austin.craigslist.org/d/cars-trucks/search/cta?auto_make_model=dodge%20charger&max_auto_year=1970&min_auto_year=1968&query=dodge
```

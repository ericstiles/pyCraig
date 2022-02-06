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

# list

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

## filter

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

# search

Search across all or a given set of sub-domains in a specific search category

```
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
## Example 1

Default is console output

```
$ ./main.py search -d html -c electronics -s "san antonio"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ Price                                                                     ┃ Year                           ┃ Title                                                                                             
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
│ $120                                                                      │                                │ Bose Frames Tenor Sunglasses                                                                      
│ $175                                                                      │                                │ Ikegami HC-D57W / CA-450 Camcorder Recorder Camera                                                
└───────────────────────────────────────────────────────────────────────────┴────────────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────
```

### Example 2

Output is html that can be piped to a file

```
$ ./main.py search -d bowers -c electronics -s "san antonio" -o html
<!DOCTYPE html>
<html lang="pl">
  <head>
    <meta charset="utf-8" />
    <title>Results</title>
  </head>
  <body>
    <div id="date" class="main_header">
      Found 5 on 06/02/2022 17:29:14
    </div>
    <div id="id23409231" class="main_header">
      <div style="background-color:white">
        <h3>
          BOWERS & WILKINS M1
        </h3>
        <div>
          $99
        </div>
        <div>
          <a href="https://sanantonio.craigslist.org/ele/d/san-antonio-bowers-wilkins-m1/7436646308.html">
            https://sanantonio.craigslist.org/ele/d/san-antonio-bowers-wilkins-m1/7436646308.html
          </a>
        </div>
        <div>
          <img src="https://images.craigslist.org/01010_lYy72Xml2Xiz_0CI0t2_300x300.jpg" />
        </div>
      </div>
      <div style="background-color:white">
        <h3>
          BOWERS & WILKINS Zeppelin Mini/Bluetooth
        </h3>
        <div>
          $99
        </div>
        <div>
          <a href="https://sanantonio.craigslist.org/ele/d/san-antonio-bowers-wilkins-zeppelin/7440201603.html">
            https://sanantonio.craigslist.org/ele/d/san-antonio-bowers-wilkins-zeppelin/7440201603.html
          </a>
        </div>
        <div>
          <img src="https://images.craigslist.org/00Y0Y_ghpYZTYx37Qz_0t20CI_300x300.jpg" />
        </div>
      </div>
      <div style="background-color:white">
        <h3>
          Fyne Audio F703 High End Speakers
        </h3>
        <div>
          $11,500
        </div>
        <div>
          <a href="https://sanantonio.craigslist.org/ele/d/seguin-fyne-audio-f703-high-end-speakers/7438236914.html">
            https://sanantonio.craigslist.org/ele/d/seguin-fyne-audio-f703-high-end-speakers/7438236914.html
          </a>
        </div>
        <div>
          <img src="https://images.craigslist.org/00D0D_kl7m1Kowujoz_0t20CI_300x300.jpg" />
        </div>
      </div>
      <div style="background-color:white">
        <h3>
          M&K Sound S300 Monitor speakers
        </h3>
        <div>
          $4,700
        </div>
        <div>
          <a href="https://sanantonio.craigslist.org/ele/d/seguin-mk-sound-s300-monitor-speakers/7429796070.html">
            https://sanantonio.craigslist.org/ele/d/seguin-mk-sound-s300-monitor-speakers/7429796070.html
          </a>
        </div>
        <div>
          <img src="https://images.craigslist.org/00101_braHWVHNwv0z_0t20CI_300x300.jpg" />
        </div>
      </div>
      <div style="background-color:white">
        <h3>
          RARE Home Speakers
        </h3>
        <div>
          $5,000
        </div>
        <div>
          <a href="https://sanantonio.craigslist.org/ele/d/san-antonio-rare-home-speakers/7425856898.html">
            https://sanantonio.craigslist.org/ele/d/san-antonio-rare-home-speakers/7425856898.html
          </a>
        </div>
        <div>
          <img src="https://images.craigslist.org/00z0z_ihdCyUxu1ZGz_0CI0CI_300x300.jpg" />
        </div>
      </div>
    </div>
  </body>
</html>


```


# example request to match
```
https://austin.craigslist.org/d/cars-trucks/search/cta?auto_make_model=dodge%20charger&max_auto_year=1970&min_auto_year=1968&query=dodge
```

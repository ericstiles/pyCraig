from airium import Airium
from classified import Advertisement


def output_html(results_list: list) -> str:
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t="Results")

        with a.body():
            with a.div(id="id23409231", klass='main_header'):
                for i in results_list:
                    map_advertisement_to_tag(i, a)

    html = str(a)  # casting to string extracts the value
    return html


def map_advertisement_to_tag(advertisement: Advertisement, a):
    with a.div(style="background-color:white"):
        with a.h3():
            a(advertisement.title)
        with a.div():
            a(advertisement.price)
        with a.div():
            with a.a(href='{}'.format(advertisement.link)):
                a(advertisement.link)
        if advertisement.image_list:
            with a.div():
                a.img(src=advertisement.image_list[0])

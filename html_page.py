from airium import Airium


def output_html() -> str:
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(lang="pl"):
        with a.head():
            a.meta(charset="utf-8")
            a.title(_t="Airium example")

        with a.body():
            with a.h3(id="id23409231", klass='main_header'):
                a("Hello World.")

    html = str(a)  # casting to string extracts the value

    print(html)

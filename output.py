"""
Module Docstring
"""
from classified import Advertisement
from rich.console import Console
from rich.table import Table
from rich.measure import Measurement
import html_page


class Output:
    # Constructor
    def __init__(self):
        self.value = "Output"

    def handle(self, results_list: list):
        print(self.value)
        pass


class ConsoleOutput(Output):
    def __init__(self):
        self.value = "Console"

    def create_table(self, results_list: list, console: Console) -> Table:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Price", style="dim", width=12)
        table.add_column("Year", style="dim", width=4)
        table.add_column("Title", width=30)
        table.add_column("Link", justify="right", no_wrap=False)

        for i in results_list:
            self.add_row(table, i)

        table_width = Measurement.get(console, table, console.width).maximum
        table.width = table_width

        return table

    def add_row(self, table: Table, result: Advertisement):
        table.add_row(result.price, result.year, result.title, result.link)

    def handle(self, results_list: list):
        console = Console()
        console.print(self.create_table(results_list, console))


class Html(Output):
    def __init__(self):
        self.value = "Html"

    def handle(self, results_list: list):
        # print("Not implemented: Class->" + self.value)
        html_page.output_html(results_list)
        f = open("output.html", "w")
        f.write(html_page.output_html(results_list))
        f.close()

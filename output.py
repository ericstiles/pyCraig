"""
Module Docstring
"""
from classified import Advertisement
from rich.console import Console
from rich.table import Table
from rich.measure import Measurement
from datetime import datetime

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
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.datestr = self.date.replace("/", "").replace(":", "").replace(" ", ".")


    def handle(self, results_list: list) -> str:
        return html_page.output_html(self.date, results_list)
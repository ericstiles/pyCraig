#!/usr/bin/env python
"""
Module Docstring
"""
from classified import Advertisement
from rich.console import Console
from rich.table import Table
from rich.measure import Measurement


def create_table(results_list: list, console: Console) -> Table:
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Price", style="dim", width=12)
    table.add_column("Year", style="dim", width=4)
    table.add_column("Title", width=30)
    table.add_column("Link", justify="right", no_wrap=False)

    for i in results_list:
        add_row(table, Advertisement.map_li_to_model(i))

    table_width = Measurement.get(console, table, console.width).maximum
    table.width = table_width

    return table


def add_row(table: Table, result: Advertisement):
    table.add_row(result.price, result.year, result.title, result.link)


def handle(results_list: list):
    console = Console()
    console.print(create_table(results_list, console))

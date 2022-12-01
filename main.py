#!/usr/bin/env python3

import click
import os


@click.command()
@click.option('--year', default='2022', help='The year of the puzzle')
@click.option('--day', default='01', help='The day you want to run')
def run(year, day):
    os.system(f"python {year}/day{day}.py")


if __name__ == '__main__':
    run()

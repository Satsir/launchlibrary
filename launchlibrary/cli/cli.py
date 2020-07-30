import click
from launchlibrary.main.api.api import API
from launchlibrary.main.local_files.local_files import LocalFiles


@click.group()
def cli():
    pass


@cli.command()
@click.argument("start_year", type=int)
@click.argument("end_year", type=int)
@click.option("-s/-ns", "--save/--not-save", default=False, help='Save request results.')
def get_launches(start_year, end_year, save):
    a1 = API()
    launches = a1.get_launches(start_year, end_year)
    click.echo(launches)
    lf1 = LocalFiles()
    if save:
        lf1.store_request_results(a1)


@cli.command()
def clear():
    LocalFiles.clear_all_request_results()


if __name__ == '__main__':
    cli()

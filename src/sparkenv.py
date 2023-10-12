import click
from downloader import get_versions
from installer import install_spark

@click.command()
@click.option('--list', '-l', is_flag=True, help='List all available versions for install')
@click.argument('version', required=False)
def install(**args):
    match args:
        case {'list': True}:
            get_versions()
        case{'version' : version, 'list': False}:
            install_spark(version)
            

@click.group()
def cli():
    pass

cli.add_command(install)

if __name__ == "__main__":
    cli()
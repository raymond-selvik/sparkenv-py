import click
from installer import (
    install_spark, 
    get_installed_spark, 
    set_active_version,
    get_active_version,
    get_available_versions
)
from config.app_config import init_app_config

@click.command(help='Install spark version')
@click.option('--list', '-l', is_flag=True, help='List all available versions for install')
@click.argument('version', required=False)
def install(**args):
    match args:
        case {'list': True}:
            versions = get_available_versions()
            for v in versions:
                print(v)
        case{'version' : None, 'list': False}:
            print("No version specified")
        case{'version' : version, 'list': False}:
            install_spark(version)

@click.command(help='List all installed Spark versions')
def versions():
    get_installed_spark()

@click.command(help='Get active spark version')
def version():
    version = get_active_version()
    if version is None:
        print("No spark isntallation active")
    else:
        print(f"Active: {version}")
@click.command(help='Set active spark version')
@click.argument('version', required=True)
def set_version(**args):
    try:
        set_active_version(args['version'])
    except Exception as ex:
        print(ex)

            
@click.group()
def cli():
    pass

cli.add_command(install)
cli.add_command(versions)
cli.add_command(version)
cli.add_command(set_version)

def main():
    init_app_config()
    cli()

if __name__ == "__main__":
    cli()
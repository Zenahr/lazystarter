import os
import click
from utils.misc import check_project_type, project_types, print_title, generate_project


@click.command()
@click.argument('project_type')
@click.option('--name', '-n', help="Name of your project")
@click.option('--gitignore', '-g', help="Space separated names of langauge / framework (s) you want to add gitignore rules for. " +
              "Example: -g \"python java node\"", default='')
def main(project_type: str, name: str, gitignore: str):
    """Main handler for the CLI

    :param project_type: str: 
    :param name: str: 
    :param gitignore: str: 

    """

    if not check_project_type(project_type):
        return click.echo('Invalid Project type.\nPossible project types are ' +
                          '-> ' + ', '.join(project_types))
    print_title()
    if not name and project_type.lower() == 'basic': 
        generate_project()
    elif name and project_type.lower() == 'basic':
        generate_project(name=name, gitignore_string=gitignore)


if __name__ == "__main__":
    main()

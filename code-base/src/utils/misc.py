import click
import os
from .gitignore import Gitignore
project_types = ["basic", "web", "react", "angular", "gatsby", "python"] # hardcoded project types

# Changed the ascii text to be more concise.

def print_title():
    """Prints the title to stdout"""
    click.echo(r"""
  _      _   _____   _____ _____ _   ___ _____ ___ ___ 
 | |    /_\ |_  \ \ / / __|_   _/_\ | _ |_   _| __| _ \
 | |__ / _ \ / / \ V /\__ \ | |/ _ \|   / | | | _||   /
 |____/_/ \_/___| |_| |___/ |_/_/ \_|_|_\ |_| |___|_|_\


""")



def check_project_type(project_type: str) -> bool:
    if project_type.lower() in project_types:
        return True
    return False

def basic_project(project_name: str, gitignores: list) -> bool:
    """Function to create the `basic` project."""
    g = Gitignore()
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        os.chdir(project_name)
        for gitignore in gitignores:
            g.gitignore_to_file(gitignore)
        os.makedirs('src')
        return True
    else:
        click.echo("[ERROR] A project already exists with the name  '" +
                   project_name + "' ")
        return False


def generate_project(name: str = '', gitignore_string: str = ''):
    """Function to provide prompts and printing progress."""
    if name == '':
        project_name = input("Project Name: ")

    elif name:
        project_name = name
        gitignores = gitignore_string.split(' ')

    if gitignore_string == '':
        if (input('Do you wish to add a .gitignore file (y/n)?: ').lower() == 'y'):
            gitignores = input(
                'Enter gitignore(s) to add to your project: ').split(' ')
        else:
            gitignores = []
    else:
        gitignores = gitignore_string.split(' ')

    click.echo("Creating Project...")
    if basic_project(project_name, gitignores):
        click.echo("Finished Creating Project")
        click.echo("[Summary of Project]")
        click.echo("Project Name: " + project_name)
        click.echo("Project Type: Web-app")
        click.echo("Project Location: " + os.getcwd())

import os
import click

# Mainloop
@click.command()
@click.argument('input')
@click.option('--type', '-t', 'project_type')
@click.option('--name', '-n', 'name')
def main(input, project_type, name): 
    input = input.lower()
    project_type = project_type.lower()
    if input == "create" and check_project_type(project_type):
        if(project_type == "basic"):
            basic_project(name)
    elif input == "prompt":
        title_screen()
        ask_for_project_name()
    else:
        print("Invalid flags!")


# Helper Functions
# ------------------------------------------------------------------

"""First screen the user will see"""
def title_screen():
    print("\n\n  _                      _____ _             _            \n | |                    / ____| |           | |           \n | |     __ _ _____   _| (___ | |_ __ _ _ __| |_ ___ _ __ \n | |    / _` |_  / | | |\___ \| __/ _` | '__| __/ _ \ '__|\n | |___| (_| |/ /| |_| |____) | || (_| | |  | ||  __/ |   \n |______\__,_/___|\__, |_____/ \__\__,_|_|   \__\___|_|   \n                   __/ |                                  \n                  |___/                                   \n\n")

def ask_for_project_name():
    project_name = input("Project Name: ") 
    print("Creating Project...") 
    if basic_project(project_name):
        print("Finished Creating Project") 
        print("[Summary of Project]") 
        print("Project Name: " + project_name) 
        print("Project Type: Web-app") 
        print("Project Location: " + os.getcwd())

def createDirectory(project_name):
    """
    Creates the root directory to store the web app
    """
    if not os.path.exists(project_name):
        os.makedirs(project_name)
    else:
        print("[ERROR] A project already exists with the name  '" + project_name + "' ")

def basic_project(project_name):
    if not os.path.exists(project_name):
        os.makedirs(project_name)
        os.chdir(project_name)
        open('.gitignore', 'a').close()
        os.makedirs('src')
    else:
        print("[ERROR] A project already exists with the name  '" +
              project_name + "' ")

def check_project_type(project_type):
    """Check for project types (basic, react, web, etc... here)"""
    available_project_types = ["basic", "web", "react", "angular", "gatsby"]
    project_type = project_type.lower()
    if project_type in available_project_types:
        return True
    return False

# Code execution
# ------------------------------------------------------------------
main()

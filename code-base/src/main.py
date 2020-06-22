import os
import click

projTypes = ["basic", "web", "react", "angular", "gatsby"]


# Mainloop
@click.command()
@click.argument('input')
@click.option('--type', '-t', 'pType')
@click.option('--name', '-n', 'name')
def main(input, pType, name): 
    input = input.lower()
    if input == "create" and checkProjType(pType.lower()):
        """Check for project types (basic, react, web, etc... here)"""
        if(pType == "basic"):
            basicProject(name)
    elif input == "prompt":
        titleScreen()
        askForProjectName()
    else:
        print("Invalid flags!")



# Helper Functions
# ------------------------------------------------------------------

"""First screen the user will see"""
def titleScreen():
    print("\n\n  _                      _____ _             _            \n | |                    / ____| |           | |           \n | |     __ _ _____   _| (___ | |_ __ _ _ __| |_ ___ _ __ \n | |    / _` |_  / | | |\___ \| __/ _` | '__| __/ _ \ '__|\n | |___| (_| |/ /| |_| |____) | || (_| | |  | ||  __/ |   \n |______\__,_/___|\__, |_____/ \__\__,_|_|   \__\___|_|   \n                   __/ |                                  \n                  |___/                                   \n\n")

def askForProjectName():
    projectName = input("Project Name: ") 
    print("Creating Project...") 
    if basicProject(projectName):
        print("Finished Creating Project") 
        print("[Summary of Project]") 
        print("Project Name: " + projectName) 
        print("Project Type: Web-app") 
        print("Project Location: " + os.getcwd())



# Your Addition
# ------------------------------------------------------------------

def createDirectory(projectName):
    """
    Creates the root directory to store the web app
    """
    if not os.path.exists(projectName):
        os.makedirs(projectName)
    else:
        print("[ERROR] A project already exists with the name  '" + projectName + "' ")


def basicProject(projectName):
    if not os.path.exists(projectName):
        os.makedirs(projectName)
        os.chdir(projectName)
        open('.gitignore', 'a').close()
    else:
        print("[ERROR] A project already exists with the name  '" +
              projectName + "' ")

def checkProjType(pType):
    if pType.lower() in projTypes:
        return True
    return False

# Code execution
# ------------------------------------------------------------------
main()

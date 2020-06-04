import os


# Mainloop
def main():
    titleScreen()
    askForProjectName()


# Helper Functions
# ------------------------------------------------------------------
"""First screen the user will see"""


def titleScreen():
    print("\n\n  _                      _____ _             _            \n | |                    / ____| |           | |           \n | |     __ _ _____   _| (___ | |_ __ _ _ __| |_ ___ _ __ \n | |    / _` |_  / | | |\___ \| __/ _` | '__| __/ _ \ '__|\n | |___| (_| |/ /| |_| |____) | || (_| | |  | ||  __/ |   \n |______\__,_/___|\__, |_____/ \__\__,_|_|   \__\___|_|   \n                   __/ |                                  \n                  |___/                                   \n\n")


def askForProjectName():
    projectName = input("Project Name: ")
    print("Creating Project...")
    if createDirectory(projectName):
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
        print("[ERROR] A project already exists with the name  '" +
              projectName + "' ")


# Code execution
# ------------------------------------------------------------------
main()

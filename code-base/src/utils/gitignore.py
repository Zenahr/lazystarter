import requests
import os
import git
import click


def get_gitignore_path() -> str:
    """Helper function to get the actual local gitignore repository."""
    file_dir = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))

    return os.path.join(file_dir, 'gitignore')


class Gitignore:
    def __init__(self):
        self.gitignore_path = get_gitignore_path()

    def update(self) -> None:
        """A function to update the gitignore submodule.
        (Can be found here: https://github.com/github/gitignore)

        """
        repo = git.Repo(self.gitignore_path)
        current = repo.head.commit
        repo.remotes.origin.pull()
        if current != repo.head.commit:
            click.echo('gitignores have been updated.')

    def append_to_file(self, file_path: str, content: str) -> None:
        """Function to append contents of gitignore to an 
        already created gitignore.
        """
        f = open(file_path, 'a')
        f.write(content)

        f.close

    def gitignore_to_file(self, name: str) -> None:
        """Helper function to find a matching .gitignore specified `name`; 
        then make a .gitignore and copy its contents to the newly created file
        """
        for root, dirs, files in os.walk(self.gitignore_path):
            for f in files:
                if f.endswith('.gitignore') and name.lower() in f.lower():
                    path = os.path.join(root, f)
                    gitignore = open(path, 'r')
                    content = gitignore.read()
                    gitignore.close()
                    self.append_to_file(os.path.join(
                        os.getcwd(), '.gitignore'), content)
                    click.echo(f'Added {f}')
                    return
        else:
            click.echo(f'Unable to find predefined gitignore for: {name}')


# Testing was done
# g = Gitignore()
# g.gitignore_to_file('python')
# g.gitignore_to_file('node')
# g.gitignore_to_file('nodesdslfhsfSOMETHINGINVALID')


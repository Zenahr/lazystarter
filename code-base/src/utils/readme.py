import os
import click

class Readme:
    def __init__(self, name, type, tech):
        self.name = name
        self.type = type
        self.tech = tech
        
    def write(self):
        with open('README.md', 'w') as readme:
            readme.write('aaaaaaaa')
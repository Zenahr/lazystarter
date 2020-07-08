import os
import click
from mdutils.mdutils import MdUtils
from mdutils import Html

class Readme:
    def __init__(self, name, type, tech):
        self.name = name
        self.type = type
        self.tech = tech
        
    def write(self):
        newRM = MdUtils(file_name='README', title='README')
        newRM.new_header(level=1, title='Overview')
        newRM.new_paragraph("Welcome to " + self.name + ", a " + self.type + " project made using [lazystarter](https://github.com/Zenahr/lazystarter), the static site generator for people who can't be bothered.")
        newRM.new_paragraph()
        newRM.new_header(level=1, title='Dependencies')
        if(self.type == "basic"):
            newRM.new_paragraph("This being a basic project, it should not require anything other than the base html, css, and javascript.")
        newRM.create_md_file()
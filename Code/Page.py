# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:52:08 2021.

@author: david
"""

import jinja2
from jinja2 import Template
from os import path
from datetime import datetime


class Page:
    """Represents one page of a document or presentation."""

    TEMPLATE_LOCATION = "../Templates"
    HTML_LOCATION = "../Output"

    def __init__(self):

        self.template = None
        self.fields = {}

        return

    def addField(self, fields: dict) -> None:
        """Add one ore more fields to the Page."""
        self.fields = {**self.fields, **fields}

    def __loadTemplate(templateName: str) -> Template:
        templateLoader = jinja2.FileSystemLoader(
            searchpath=Page.TEMPLATE_LOCATION)
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template(templateName+".html")

        return template

    def makeTestPage():
        """Create a test page object."""
        testHTML = Page.__loadTemplate("BasicTemplate")
        newPage = Page()
        newPage.template = testHTML
        newPage.addField({
            "css": "body {background-color: gray}",
            "body": "Hello, World!"})

        return newPage

    def render(self, name: str = None) -> str:
        """
        Render the page to an HTML file.

        Returns that file's address
        """
        if name is None:
            name = datetime.utcnow().strftime('%Y-%m-%d %H%M%S%f')[:-3]

        newFileName = path.join(Page.HTML_LOCATION, name+".html")
        htmlCode = self.template.render(**self.fields)
        html_file = open(newFileName, 'w')
        html_file.write(htmlCode)
        html_file.close()

        return newFileName


if __name__ == "__main__":
    newPage = Page.makeTestPage()
    fileLoc = newPage.render("testHTML")
    print(newPage.fields)
    print(fileLoc)

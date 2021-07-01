# -*- coding: utf-8 -*
"""
Created on Tue Jun 29 21:51:27 2021.

@author: david
"""

from Page import Page
import pdfkit
from os import path
from datetime import datetime


class Document:
    """Represents an entire document or presentation."""

    PDF_LOCATION = "../Output"

    def __init__(self):
        self.pages = []
        return

    def addPage(self, page: Page):
        """Add a Page to the document."""
        self.pages.append(page)
        return

    def toPDF(self, name: str = None):
        """Render the document to PDF."""
        options = {
          "enable-local-file-access": None
        }
        if name is None:
            name = datetime.utcnow().strftime('%Y-%m-%d %H%M%S%f')[:-3]

        newFileName = path.join(Document.PDF_LOCATION, name+".pdf")

        htmlFiles = []
        for page in self.pages:
            htmlFiles.append(page.render())

        pdfkit.from_file(htmlFiles, newFileName, options=options)
        return


if __name__ == "__main__":
    myDoc = Document()

    for i in range(3):
        myDoc.addPage(Page.makeTestPage())

    myDoc.toPDF("testPDF")

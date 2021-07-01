# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:11:46 2021.

@author: david
"""


class Field:
    """Represents a single content field on a Page."""

    def __init__(self, 
                 contents: str,
                 htmlID: str = None,
                 htmlClass: list = []):
        self.contents = contents
        self.htmlID = htmlID
        self.htmlClass = htmlClass
        return

    def addClass(self, htmlClass: str) -> None:
        """Add a class to this Field."""
        self.htmlClass.append(htmlClass)
        return

    def getHTML(self) -> str:
        """Get the HTML code that represents this Field."""
        message = "<div"
        if self.htmlID is not None:
            message += ' id="'+self.htmlID+'"'

        if len(self.htmlClass) > 0:
            message += ' class ="'
        for curClass in self.htmlClass:
            message += curClass + ' '
        if len(self.htmlClass) > 0:
            message += '"'

        message += ">"

        message += self.contents

        message += "</div>"

        return message
    
    def makeBasicField():
        return Field("Hello World!")

if __name__=="__main__":
    testField = Field.makeBasicField()
    print(testField.getHTML())
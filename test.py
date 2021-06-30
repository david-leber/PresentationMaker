# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:54:53 2021

@author: david
"""

import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "test.txt"
template = templateEnv.get_template(TEMPALTE_FILE)
outputText = template.render(name="David Leber")
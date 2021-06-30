# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:54:53 2021

@author: david
"""

import pandas as pd
import pdfkit
import jinja2
import seaborn as sns
import matplotlib.pyplot as plt
import os

DO_CLEAN_UP = True
PNG_RESOLUTION = 100

print("Creating the dataframes.")
interest_rates = [i*.01 for i in range(1,11)]
initial_account_sizes = [100, 500, 20000, 50000]
data_frames = []
for interest_rate in interest_rates:
    df = {}
    for initial_account_size in initial_account_sizes:
        df['Account Size: ' + str(initial_account_size)] = [initial_account_size * (1 + interest_rate) ** year for year in range(1, 21)]
    df = pd.DataFrame(df)
    df.index.name = 'year'
    data_frames.append({'df':df,
        'interest_rate':interest_rate})
    
print("Reading in the Jinja template.")
templateLoader = jinja2.FileSystemLoader(searchpath="../Templates/")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "test.html"
template = templateEnv.get_template(TEMPLATE_FILE)

print("Generating the HTML files.")
filesGenerated = []
tempFilesGenerated = []
for d in data_frames:
    
    newFileNameBase = "../Output/"+str(int(d['interest_rate'] * 100))
    newFileName = newFileNameBase+".html"
    imageFileName = newFileNameBase+'png.png'
    
    fig = plt.figure()
    snsPlot = sns.lineplot(data=d['df'])
    snsFig = snsPlot.get_figure()
    snsFig.savefig(imageFileName, dpi=PNG_RESOLUTION)
    plt.show()
    
    outputText = template.render(df=d['df'],
            interest_rate=d['interest_rate'],
            imageSource=imageFileName)
    html_file = open(newFileName, 'w')
    html_file.write(outputText)
    html_file.close()
    filesGenerated.append(newFileName)
    tempFilesGenerated.append(newFileName)
    tempFilesGenerated.append(imageFileName)

print("Generating the PDF.")

options = {
  "enable-local-file-access": None
}
pdfkit.from_file(filesGenerated, '../Output/test.pdf', options=options)

if DO_CLEAN_UP:
    print("Cleaning up temporary files.")
    for file in tempFilesGenerated:
        os.remove(file)

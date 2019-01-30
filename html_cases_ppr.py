#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################
# Scrap case number from html extracted from myimmitracker
###################################################################

from bs4 import BeautifulSoup

# Get the case data
with open('input_cases.html', 'r') as myfile:
    data=myfile.read()

file = open("output_cases.txt","w") # Output file for found cases

# Load data into BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

ignoredStreams = ['CEC', 'FSW-Inland', 'PNP-Inland', 'PNP-Outland']
parsedStreams = ['FSW-Outland']
parsedIndex = []

i = 1
for span in soup.find_all('span'):

    if(span.text.strip() in ignoredStreams):
        i += 1
    if(span.text.strip() in parsedStreams):
        parsedIndex.append(i)
        i += 1

i = 1
for a in soup.find_all('a', href=True):

    if('/ca/trackers/consolidated-e-apr-tracker-express-entry-permanent-residency-application/cases/case-' in a['href']):
        if(i in parsedIndex):
            file.write('\"' + a['href'][-5:] + '\",' + '\n') # Save the case number if it is not from an ignored stream
        i += 1

file.close()

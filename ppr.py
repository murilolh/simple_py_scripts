#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############################################
# Scrap data from cases at myimmitracker
#############################################

import requests
import json
from bs4 import BeautifulSoup

cases = json.loads(open('input_ppr.json').read()) # JSON file that contain the cases to be analysed

file = open("output_ppr.txt","w") # Output file for analysed cases

# PPR Date	AOR Date	Number of Days	Nationality	Residence	Office	PA + Dep	ADR Date	PPR from ADR	SS
fields = [16, 7, 10, 6, 8, 17 , 15, 31, 32, 36] # List of fields, in order, to be printed

for case in cases:
    # Get the case data
    data = requests.get('https://myimmitracker.com/en/ca/trackers/consolidated-e-apr-tracker-express-entry-permanent-residency-application/cases/case-' + case)

    # Load data into BeautifulSoup
    soup = BeautifulSoup(data.text, 'html.parser')

    # Reaching the div that contain the data
    detdiv = soup.find('div', { 'class': 'details' })
    casesdiv = detdiv.find_all('div')[41]
    datadiv = casesdiv.find_all('div')

    #print 'Printing case ' + case
    for field in fields:
        file.write(datadiv[field].text.strip() + '\t')
    file.write(case + '\n')

file.close()

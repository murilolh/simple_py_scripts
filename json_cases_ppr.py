#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################
# Scrap case number from json extracted from myimmitracker
###################################################################

import json

data = json.loads(open('input_cases.json').read()) # JSON file that contain the cases to be analysed

file = open("output_cases.json","w") # Output file for found cases

for value in data["values"]:
    file.write("\t\"" + value["username"][1][-5:] + "\",\n")

file.close()

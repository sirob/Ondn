#Program for sorting my Google Analytics pageview report.

import re

#Open file and read it as a string.

def file_to_string(filename):
    filename = input("Please provide the path to the Google Analytics file:")
    file = open(filename, 'r')
    text = file.read()
    print(text)

#Catch names and number of pageviews for 20 most viewed article pages for the last week with regular expresions.

def catch_data(text):
    site_name = re.search('www.\w+.\w+', text)
    report_date = re.search('\w+-\w+', text)
    print (site_name.group())
    print (report_date.group())

#Save 20 most viewed pages in a new file.

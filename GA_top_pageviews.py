#Program for sorting my Google Analytics pageview report.

import re

#Open file and read it as a string.

filename = input("Please provide the path to the Google Analytics file:")

def file_to_string(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

#Catch names and number of pageviews article pages for the last week with regular expresions.

text = file_to_string(filename)


def catch_data(text):
    site_name = re.search('www.\w+.\w+', text)
    report_date = re.search('\w+-\w+', text)
    title = site_name.group()
    date_range = report_date.group()
    articles = re.findall('(/\w+/\D+),"(\w+,\w+)"', text)
    return title, date_range, articles
    

#Save 20 most viewed pages in a new file.

tup = catch_data(text)

def write_file(filename):
    filename = input("Please provide the path to the write-to file:")
    title = tup[0]
    date_range = tup[1]
    articles = tup[2]
    new_articles = articles[:20]
    file = open(filename, 'w')
    file.write(title + '\n\n')
    file.write(date_range + '\n\n')
    for art in new_articles:
        file.write(art[0] + ',' + ' ' + art[1] + '\n\n')
    file.close()
    

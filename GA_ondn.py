#Program for sorting Google Analytics pageview report.

#IMPORTANT - Precondition: Report must be exported from GA Pages (english) in .csv format

import re

#Open file and read it as a string.

def file_to_string(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

#Catch name, date, title of article and number of pageviews per article with regular expressions.

def catch_data(text):
    site_name = re.search('www.\w+.\w+', text)
    report_date = re.search('\w+-\w+', text)
    title = site_name.group()
    date_range = report_date.group()
    articles = re.findall('(/\w+/\D+),"(\w+,\w+)"', text)
    return title, date_range, articles
    

#Save "n" most viewed pages in a new file.

#Precondition: Your original report must contain a minimum of n articles.

def write_file(filewrite, n):
    title = tup[0]
    date_range = tup[1]
    articles = tup[2]
    top_articles = articles[:n]
    file = open(filewrite, 'w')
    file.write(title + '\n\n')
    file.write(date_range + '\n\n')
    for art in top_articles:
        file.write(art[0] + ',' + ' ' + art[1] + '\n\n')
    file.close()


if __name__ == "__main__":
    filename = input("Please provide the path to the Google Analytics file (without the quotes):")
    filewrite = input("Please provide the path to the write-to file (without the quotes):")
    n = input("The number of the articles with the most pageviews you would like to have in the new report:")
    text = file_to_string(filename)
    tup = catch_data(text)
    write_file(filewrite, int(n)) 

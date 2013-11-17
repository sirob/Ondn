#Program for sorting Google Analytics pageview report.

#IMPORTANT - Precondition: Report must be exported from GA Pages (english) in .csv format

import re
from datetime import datetime

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


#Remove listed subcategories from the articles list in the tuple.

def clear_subcat(old_tup):
    title = old_tup[0]
    date_range = old_tup[1]
    articles = old_tup[2]
    clear_articles = [x for x in articles if x[0] not in ('/slovenija/v-ospredju', '/sport/nogomet',
                                                          '/poslovni/novice', '/sport/hokej-na-ledu') and '/tag/' not in x[0]]
    return title, date_range, clear_articles

    
#Save "n" most viewed pages in a new file.

#Precondition: Your original report must contain a minimum of n articles.

def write_file(filewrite, n):
    title = tup[0]
    date_range = tup[1]
    range_start, range_end = date_range[:8], date_range[9:]
    date_start = datetime.strptime(range_start, '%Y%m%d')
    date_end = datetime.strptime(range_end, '%Y%m%d')
    articles = tup[2]
    top_articles = articles[:n]
    file = open(filewrite, 'w')
    file.write(title + '\n\n')
    file.write('From: ' + str(date_start) + ' To: ' + str(date_end) + '\n\n')
    for art in top_articles:
        file.write(art[0] + ',' + ' ' + art[1] + '\n\n')
    file.close()


if __name__ == "__main__":
    filename = input("Please provide the path to the Google Analytics file (without the quotes):")
    filewrite = input("Please provide the path to the write-to file (without the quotes):")
    n = input("Please select the number of articles with the most pageviews you would like to have in the new report:")
    text = file_to_string(filename)
    old_tup = catch_data(text)
    tup = clear_subcat(old_tup)
    write_file(filewrite, int(n))
    print('Done!')

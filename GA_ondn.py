#Program for sorting Google Analytics pageview report.

#IMPORTANT - Precondition: Report must be exported from GA Pages (english) in .csv format

import re
import sys
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
    articles = re.findall('(/\D+/[^,]+),"(\w+,\w+)"', text)
    return title, date_range, articles


#Remove listed subcategories from the articles list in the tuple.

def clear_subcategories(articles):
    clear_articles = [x for x in articles if x[0] not in ('/slovenija/v-ospredju', '/sport/nogomet',
                                                          '/poslovni/novice', '/sport/hokej-na-ledu,') and '/tag/' not in x[0]]
    return clear_articles

    
#Save "n" most viewed pages in a new file.

#Precondition: Your original report must contain a minimum of n articles.

def write_file(title, date_range, articles, filewrite, n):
    range_start, range_end = date_range[:8], date_range[9:]
    date_start = datetime.strptime(range_start, '%Y%m%d')
    date_end = datetime.strptime(range_end, '%Y%m%d')
    top_articles = articles[:n]

    # file = open(filewrite, 'w')
    # file.write(title + '\n\n')
    # file.write('From: ' + str(date_start) + ' To: ' + str(date_end) + '\n\n')
    # for art in top_articles:
    #     file.write(art[0] + ',' + ' ' + art[1] + '\n\n')
    # file.close()

    with open(filewrite, 'w') as file:
        file.write(title + '\n\n')
        file.write('From: ' + str(date_start) + ' To: ' + str(date_end) + '\n\n')
        for art in top_articles:
            file.write(art[0] + ',' + ' ' + art[1] + '\n\n')



if __name__ == "__main__":
    if len(sys.argv) < 4:
        print ("Please provide input file, output file and the number of articles you want to have in your output file.")
        sys.exit(0)

    # filename = input("Please provide the path to the Google Analytics file (without the quotes):")
    filename = sys.argv[1]
    # filewrite = input("Please provide the path to the write-to file (without the quotes):")
    filewrite = sys.argv[2]
    # n = input("Please select the number of articles with the most pageviews you would like to have in the new report:")
    n = sys.argv[3]

    # text = file_to_string(filename)
    text = open(filename, 'r').read()

    title, date_range, articles = catch_data(text)
    articles = clear_subcategories(articles)
    write_file(title, date_range, articles, filewrite, int(n))
    print('Done!')

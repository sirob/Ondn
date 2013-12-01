from GA_ondn import catch_data, file_to_string, clear_subcategories
import urllib.request
import re
import sys
import html.parser


def get_article_list(filename):
    ''' (str) -> tuple
    Returns a tuple containing a part of url and number of pageviews
    extracted from the csv file.
    '''
    text = file_to_string(filename)
    title, date_range, articles = catch_data(text)
    articles = clear_subcategories(articles)
    return articles


def get_urls(filename):
    ''' (str) -> list of str
    Returns a list of www.dnevnik.si full urls.
    '''
    li = get_article_list(filename)
    urls = [('http://www.dnevnik.si') + x[0] for x in li]
    return urls

def fetch_title(url):
    ''' (str) -> str
    Gets the source code of a webpage of a given url and returns
    the title of the page, extracted with regular expressions.
    '''
    response = urllib.request.urlopen(url)
    html = response.read()
    text = html.decode('utf-8')
    match = re.search("<title>(.+)<", text)
    return match.group(1)

def get_titles(articles):
    ''' (str) -> list of str
    Returns the list of webpage titles from the urls in the csv file.
    '''
    h = html.parser.HTMLParser()

    articles = [('http://www.dnevnik.si') + x[0] for x in articles]

    titles_non = [fetch_title(x) for x in articles]
    titles = [h.unescape(x) for x in titles_non]
    return titles

def get_pageviews(li):
    ''' (str) -> list of str
    Returns a list of pageviews for each of the urls from csv file.
    '''
    pageviews = [x[1] for x in li]
    return pageviews

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please, provide the input file.')
        sys.exit()

    # filename = input("Path to file:")
    filename = sys.argv[1]

    articles = get_article_list(filename)
    # titles = get_titles(filename)
    titles = get_titles(articles)
    pageviews = get_pageviews(articles)
    titles_pageviews = zip(titles, pageviews)
    for x in titles_pageviews:
        print(x)

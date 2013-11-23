from GA_ondn import catch_data, file_to_string, clear_subcat
import urllib.request
import re
import html.parser


def get_article_list(filename):
    ''' (str) -> tuple
    Returns a tuple containing a part of url and number of pageviews
    extracted from the csv file.
    '''
    text = file_to_string(filename)
    tup = catch_data(text)
    clear_tup = clear_subcat(tup)
    return clear_tup[2]


def get_urls(filename):
    ''' (str) -> list of str
    Returns a list of www.dnevnik.si full urls.
    '''
    li = get_article_list(filename)
    urls = [('http://www.dnevnik.si') + x[0] for x in li]
    return urls

def get_pageviews(filename):
    ''' (str) -> list of str
    Returns a list of pageviews for each of the urls from csv file.
    '''
    li = get_article_list(filename)
    pageviews = [x[1] for x in li]
    return pageviews

def get_title(url):
    ''' (str) -> str
    Gets the source code of a webpage of a given url and returns
    the title of the page, extracted with regular expressions.
    '''
    response = urllib.request.urlopen(url)
    html = response.read()
    text = html.decode('utf-8')
    match = re.search("<title>(.+)<", text)
    return match.group(1)

def get_titles(filename):
    ''' (str) -> list of str
    Returns the list of webpage titles from the urls in the csv file.
    '''
    h = html.parser.HTMLParser()
    titles_non = [get_title(x) for x in get_urls(filename)]
    titles = [h.unescape(x) for x in titles_non]
    return titles

    
if __name__ == "__main__":
    filename = input("Path to file:")
    urls = get_urls(filename)
    titles = get_titles(filename)
    pageviews = get_pageviews(filename)
    titles_pageviews = zip(titles, pageviews)
    for x in titles_pageviews:
        print(x)

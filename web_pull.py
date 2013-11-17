from GA_ondn import catch_data, file_to_string
import urllib.request
import re

def get_title(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    text = html.decode('utf-8')
    match = re.search("<title>(.+)<", text)
    return match.group(1)

if __name__ == "__main__":
    filename = input("Path to file:")
    text = file_to_string(filename)
    tup = catch_data(text)
    li = tup[2]
    cli = [('http://www.dnevnik.si') + x[0] for x in li]
    titles = [get_title(x) for x in cli]
    print (titles)



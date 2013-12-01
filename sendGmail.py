import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from web_pull import *
from datetime import datetime
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide the input file.')
        sys.exit()

    filename = sys.argv[1]
    text = file_to_string(filename)
    tup = catch_data(text)
    date_range = tup[1]
    range_start, range_end = date_range[:8], date_range[9:]
    date_start = datetime.strptime(range_start, '%Y%m%d')
    date_end = datetime.strptime(range_end, '%Y%m%d')
    
    urls = get_urls(filename)
    articles = get_article_list(filename)
    titles = get_titles(articles)
    pageviews = get_pageviews(articles)

    fromaddr = 'xxxxx@gmail.com'        #Replace with your gmail account.
    toaddr = 'some@email.com'           #Replace with the address you want to send to.
    msg = MIMEMultipart('alternative')

    msg['To'] = toaddr
    msg['From'] = fromaddr
    msg['Subject'] = Header('Najbolj brani članki preteklega tedna', 'utf-8')

    html = """
    <html>
      <head></head>
      <body>
        <p>Od: %s Do: %s</p>""" % (str(date_start), str(date_end))

    for i in range(0,20):
        html += '<h1> %s. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>\n' % (i+1, titles[i], urls[i], pageviews[i])
        



    msg.attach(MIMEText(html.encode('utf-8'), 'html', 'utf-8'))


    username = 'xxxxxx@gmail.com'    #Replace with your gmail account.
    password = 'xxxxxxxx'       #Replace with application password: https://support.google.com/accounts/answer/185833
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
    print("Email has been sent.")

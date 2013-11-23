import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from web_pull import *
from datetime import datetime


if __name__ == "__main__":
    filename = input("Please, provide the path to the file:")
    text = file_to_string(filename)
    tup = catch_data(text)
    date_range = tup[1]
    range_start, range_end = date_range[:8], date_range[9:]
    date_start = datetime.strptime(range_start, '%Y%m%d')
    date_end = datetime.strptime(range_end, '%Y%m%d')
    
    urls = get_urls(filename)
    titles = get_titles(filename)
    pageviews = get_pageviews(filename)

    fromaddr = 'xxxxxx@gmail.com'
    toaddr = 'some@email.com'
    msg = MIMEMultipart('alternative')

    msg['To'] = toaddr
    msg['From'] = fromaddr
    msg['Subject'] = Header('Najbolj brani članki preteklega tedna', 'utf-8')

    html = """\
    <html>
      <head></head>
      <body>
        <p>Od: %s Do: %s</p>
        <h1> 1. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 2. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 3. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 4. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 5. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 6. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 7. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 8. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1> 9. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>10. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>11. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>12. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>13. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>14. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>15. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>16. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>17. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>18. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>19. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
        <h1>20. %s <a href="%s">-klik-</a> %s ogledov</h1></br></br>
      </body>
    </html>
    """ %(str(date_start), str(date_end), titles[0], urls[0], pageviews[0], titles[1], urls[1], pageviews[1],
          titles[2], urls[2], pageviews[2], titles[3], urls[3], pageviews[3],
          titles[4], urls[4], pageviews[4], titles[5], urls[5], pageviews[5],
          titles[6], urls[6], pageviews[6], titles[7], urls[7], pageviews[7],
          titles[8], urls[8], pageviews[8], titles[9], urls[9], pageviews[9],
          titles[10], urls[10], pageviews[10], titles[11], urls[11], pageviews[11],
          titles[12], urls[12], pageviews[12], titles[13], urls[13], pageviews[13],
          titles[14], urls[14], pageviews[14], titles[15], urls[15], pageviews[15],
          titles[16], urls[16], pageviews[16], titles[17], urls[17], pageviews[17],
          titles[18], urls[18], pageviews[18], titles[19], urls[19], pageviews[19])


    msg.attach(MIMEText(html.encode('utf-8'), 'html', 'utf-8'))


    username = 'xxxxx@gmail.com'
    password = ' xxxxxxxxxx'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
    print("Email has been sent.")

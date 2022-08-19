import requests
from bs4 import BeautifulSoup
import time
import cssutils
from urllib.parse import urlparse

url = 'https://www.osulzer.at/blog'

def get_blog_content(url):
    content = get_url_content(url)
    # übergebe html an beautifulsoup parser
    soup = BeautifulSoup(content, "html.parser")

    for post in soup.findAll('div', {'class': 'blog-post'}):

        # Übergebe inline css an cssutils für einfaches auslesen der attribute
        bg = cssutils.parseStyle(post.find('a').get('style'))
        title = post.find('h2').text
        link = post.find('a').get('href')
        image = bg['background-image'].replace('url(', '').replace(')', '')

        print('Title: %s' % title)

        # mithilfe von .get können attribute des "a" elements ausgelesen werden
        print('Link: %s' % link)

        # der ausgelesene Bild-Link enthält noch ungewollte styling attribute die wir einfach löschen
        print('Image: %s' % image)

        get_blog_post(get_domain(url) + link)


def get_blog_post(url):
    content = get_url_content(url)
    soup = BeautifulSoup(content, "html.parser")

    # extrahiere den inhalt aus dem div mit der klasse textcontent
    text = soup.find('div', {'class': 'textcontent'}).text

    # ersetze sonderzeichen mit leerzeichen
    for char in '=+-.,\n':
        text = text.replace(char, ' ')
    text = text.lower().split()

    # gibt die länge des aus split resultierendem list elements aus
    print('Wörter: %s' % len(text))



# gibt html code der gewünschten url zurück
def get_url_content(url):
    # wartet 1 Sekunde zwischen jeder anfrage
    time.sleep(1)
    return requests.get(url).text

def get_domain(url):
    parsed_uri = urlparse(url)
    return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)


get_blog_content(url)
from requests import get
from bs4 import BeautifulSoup
import sys

URL = 'https://www.instagram.com'

def get_data(username):
    url = '%s/%s/' % (URL, username)
    page = get(url, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('meta', attrs={'property': 'og:description'})
    photo = soup.find_all('meta', attrs={'property': 'og:image'})
    text = data[0].get('content').split()
    return {
        'name':'%s %s' % (text[-2], text[-1]),
        'posts': text[4],
        'followers': text[0],
        'following': text[2],
        'photo_url': photo[0].get('content')
    }

if __name__ == '__main__':
    print(get_data(str(sys.argv[1])))

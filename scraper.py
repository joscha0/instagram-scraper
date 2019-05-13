from requests import get
from bs4 import BeautifulSoup
import sys
import re
import json

URL = 'https://www.instagram.com'

def get_data(username):
    url = '%s/%s/' % (URL, username)
    page = get(url, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('meta', attrs={'property': 'og:description'})
    photo = soup.find_all('meta', attrs={'property': 'og:image'})
    text = data[0].get('content').split()
    retext = re.findall('<script type="text\/javascript">([^{]+?({.*profile_pic_url.*})[^}]+?)<\/script>', str(soup))[0][1]
    jsontext = json.loads(retext)['entry_data']['ProfilePage'][0]
    return {
        'name' : username,
        'bio' : jsontext['graphql']['user']['biography'],
        'url' : jsontext['graphql']['user']['external_url'],
        'is_business' : jsontext['graphql']['user']['is_business_account'],
        'posts': text[4],
        'followers': text[0],
        'following': text[2],
        'photo_url': photo[0].get('content'),
        'followerCount' : jsontext['graphql']['user']['edge_followed_by']['count'],
        'followingCount' : jsontext['graphql']['user']['edge_follow']['count'],
        'postCount' : jsontext['graphql']['user']['edge_owner_to_timeline_media']['count'],

    }

if __name__ == '__main__':
    data = get_data(str(sys.argv[1]))
    for key in data: 
        print('\033[1m' + key + '\033[0;0m'+ '\n' + str(data[key])+'\n')
    

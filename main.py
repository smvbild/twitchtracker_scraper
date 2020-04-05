from bs4 import BeautifulSoup
import requests

def scrape_data():
    hdr = {'User-Agent':'Mozilla/5.0'}
    page = requests.get('https://twitchtracker.com/channels/viewership', headers=hdr)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    names = soup.findAll('div', {'class': 'ri-name'})

    for name in names:
        link = name.find('a', href=True)
        link = f'https://twitchtracker.com{link["href"]}'
        streamer_page = requests.get(link, hdr)
        streamer_soup = BeautifulSoup(streamer_page.content, 'html.parser')

        streamer_statlist = streamer_soup.find('ul', {'class':'list-group text-center'})
        streamer_stats = streamer_statlist.findAll('li')
        for index, stat in enumerate(streamer_stats):
            print('#'*100)
            print(index)
            print(stat.text.strip().split())

def main():
    scrape_data()

if __name__ == '__main__':
    main()

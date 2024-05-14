import requests
from bs4 import BeautifulSoup

URL = 'https://www.hltv.org/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

def find_team_games(team):
    pass


def matches_today():
    response = requests.get(URL, headers=headers,  timeout=30)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        todays_matches = soup.find('h1', class_='clearfix todaysMatches').find_parent('aside').find_all('a')

        print(todays_matches)


def main():
    matches_today()


if __name__ == "__main__":
    main()

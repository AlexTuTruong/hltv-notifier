import requests
from bs4 import BeautifulSoup


URL = 'https://www.hltv.org/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def matches_today():
    response = requests.get(URL, headers=headers,  timeout=30)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        matches = soup.find('h1', class_='clearfix todaysMatches').find_parent('aside').find_all('a')[1:]

        match_dicts = []
        for match in matches:

            teams = match.find_all('div', class_='teamrow')

            dict = {
                'Series': match.get('title'),
                'Team 1': teams[0].text,
                'Team 2': teams[1].text,
                'Date/Time': match.find('div', class_='middleExtra').get('data-unix') if match.find('div', class_='middleExtra') else 'Match is Live'
            }

            match_dicts.append(dict)

    return match_dicts


def main():
    matches = matches_today()

    for match in matches:
        print(match)


if __name__ == "__main__":
    main()

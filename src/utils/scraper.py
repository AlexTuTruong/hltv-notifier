import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL = "https://www.hltv.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


def matches_today():
    response = requests.get(URL, headers=headers, timeout=30)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        matches = (
            soup.find("h1", class_="clearfix todaysMatches")
            .find_parent("aside")
            .find_all("a")[1:]
        )

        match_dicts = []
        for match in matches:

            teams = match.find_all("div", class_="teamrow")
            date = int(
                match.find("div", class_="middleExtra").get("data-unix")
                if match.find("div", class_="middleExtra")
                else "0"
            )

            if date == 0 or within_day(date):
                if date == 0:
                    time = "Live"
                else:
                    date_time = datetime.fromtimestamp(date / 1000)
                    time = date_time.strftime("%H:%M")

                dict = {
                    "Series": match.get("title"),
                    "Team 1": teams[0].text[1:],
                    "Team 2": teams[1].text[1:],
                    "Time": time,
                }

                match_dicts.append(dict)

    return match_dicts


def within_day(unix_timestamp):
    date_time = datetime.fromtimestamp(unix_timestamp / 1000)
    now = datetime.now().date()
    day_start = datetime.combine(now, datetime.min.time())
    day_end = datetime.combine(now, datetime.max.time())

    return day_start <= date_time <= day_end


def main():
    matches = matches_today()

    for match in matches:
        print(match)


if __name__ == "__main__":
    main()

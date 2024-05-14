import requests
from bs4 import BeautifulSoup
from datetime import datetime


URL = "https://www.hltv.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}


def matches_today():
    """
    Returns a list of dictionary objects, each being a match played within the day (00:00 - 23:59).
    Example object:
    dict = {
        "Series": "ESL Challenger League Season 47 Europe",
        "Team 1": "Virtus.pro",
        "Team 2": "Falcons",
        "Time": 14:00,
    }
    """
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
                    "Team 1": teams[0].text.lstrip(),
                    "Team 2": teams[1].text.lstrip(),
                    "Time": time,
                }

                match_dicts.append(dict)

    return match_dicts


def within_day(unix_timestamp):
    """Returns true if the given unix timestamp is within the current day (00:00 - 23:59), false otherwise"""
    date_time = datetime.fromtimestamp(unix_timestamp / 1000)
    now = datetime.now().date()
    day_start = datetime.combine(now, datetime.min.time())
    day_end = datetime.combine(now, datetime.max.time())

    return day_start <= date_time <= day_end


def main():
    """Prints all matches for the current day"""
    matches = matches_today()

    for match in matches:
        print(match)


if __name__ == "__main__":
    main()

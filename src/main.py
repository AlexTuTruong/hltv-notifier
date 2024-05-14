from utils import scraper

matches = scraper.matches_today()

for match in matches:
    print(match)

from utils import scraper

TEAM = "Virtus.pro"


matches = scraper.matches_today()

matches_with_team = []
for match in matches:
    if match["team1"] == TEAM or match["team2"] == TEAM:
        matches_with_team.append(match)

for game in matches_with_team:
    print(game)

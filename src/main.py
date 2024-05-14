from utils import scraper, SMS

# TEAM = "Virtus.pro"
TEAM = "ODDIK"


matches = scraper.matches_today()

matches_with_team = []
for match in matches:
    teams = [match["Team 1"], match["Team 2"]]
    if TEAM in teams:
        matches_with_team.append(match)

for game in matches_with_team:
    message = f"{game['Series']}, {game['Team 1']} vs {game['Team 2']} @ {game['Time']}"
    print(message)

from utils import scraper, SMS
import unicodedata


# TEAM = "Virtus.pro"
TEAM = "ODDIK"


def send_matches_with_team(user_team):
    matches = scraper.matches_today()

    matches_with_team = []
    for match in matches:
        teams = [match["Team 1"], match["Team 2"]]
        if user_team in teams:
            matches_with_team.append(match)

    lines = []
    for game in matches_with_team:
        opposing_team = (
            game["Team 1"] if game["Team 1"] != user_team else game["Team 2"]
        )
        lines.append(f"vs {opposing_team} @ {game['Time']}")
        games_message = "\n".join(line for line in lines)

    games_message = replace_unicode_characters(games_message)
    formatted_message = f"Subject: {user_team} is playing!\n\n{games_message}"

    print("sending message:\n", formatted_message)
    SMS.send(formatted_message)


def replace_unicode_characters(text):
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )


send_matches_with_team(TEAM)

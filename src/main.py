from utils import scraper, SMS
from dotenv import load_dotenv
import os
import unicodedata


load_dotenv()
config_team = os.getenv("TEAM")


def send_matches_with_team(user_team):
    """
    Retrieves a list of match dictionary objects from scraper.py and sends a
    formatted SMS text if the user specified team is playing within the day (00:00 - 23:59)
    """
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
        if game["Time"] == "Live":
            lines.append(f"vs {opposing_team} Live")
        else:
            lines.append(f"vs {opposing_team} @ {game['Time']}")
        games_message = "\n".join(line for line in lines)

    games_message = replace_unicode_characters(games_message)
    formatted_message = f"Subject: {user_team} is playing!\n\n{games_message}"

    print("sending message:\n", formatted_message)
    if formatted_message:
        SMS.send(formatted_message)


def replace_unicode_characters(text):
    """Replaces unicode characters with ASCII equivalent as smtplib requires unicode encoding"""
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )


send_matches_with_team(config_team)

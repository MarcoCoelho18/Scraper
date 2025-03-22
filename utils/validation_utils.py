from thefuzz import process
from config import valid_teams, team_abbreviations
import logging

def validate_team_name(team_name):
    if team_name.upper() in team_abbreviations:
        logging.info(f"Found abbreviation: {team_name} -> {team_abbreviations[team_name.upper()]}")
        return team_abbreviations[team_name.upper()]
    
    matches = process.extract(team_name, valid_teams, limit=1)
    if matches and matches[0][1] >= 80:
        logging.info(f"Found closest match: {matches[0][0]} (Score: {matches[0][1]})")
        return matches[0][0]
    else:
        logging.warning(f"Team '{team_name}' not found. No close match found.")
        return None
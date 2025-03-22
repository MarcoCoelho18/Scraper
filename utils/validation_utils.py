from thefuzz import process
from config import valid_teams, team_abbreviations, LEAGUE_COUNTRIES
import logging

def validate_team_name(team_name, league_code):
    # Get the country for the league
    country = LEAGUE_COUNTRIES.get(league_code, "Unknown")
    
    
    # Check if the input is an abbreviation
    if team_name.upper() in team_abbreviations:
        full_name = team_abbreviations[team_name.upper()]
        return full_name, country
    
    # Use fuzzy matching to find the closest team name
    matches = process.extract(team_name, valid_teams, limit=1)
    if matches and matches[0][1] >= 80:  # Check if the match score is above a threshold (e.g., 80%)
        closest_team = matches[0][0]
        return closest_team, country
    else:
        logging.warning(f"Team '{team_name}' not found. No close match found.")
        return None, None
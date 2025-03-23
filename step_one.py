import requests
import json
from datetime import datetime
import logging
from utils.file_utils import save_to_json
from config import API_KEY, BASE_URL, MATCHES_FOLDER, LEAGUE_COUNTRIES, TEAM_NAME_MAPPING
import unicodedata

def fetch_matches_by_date(date):
    headers = {'X-Auth-Token': API_KEY}
    formatted_date = date.strftime('%Y-%m-%d')
    endpoint = f'matches?date={formatted_date}'
    response = requests.get(BASE_URL + endpoint, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to fetch data: {response.status_code}")
        return None

def normalize_text(text):
    """
    Normalizes accented characters in the text.
    Example: "Atlético Madrid" -> "Atletico Madrid"
    """
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

def map_team_name(team_name):
    """
    Maps team names to a standardized format using TEAM_NAME_MAPPING.
    """
    return TEAM_NAME_MAPPING.get(team_name, team_name)

def extract_relevant_data(matches_data):
    """
    Extracts and organizes relevant match data by league.
    Normalizes accented characters and maps team names to a standardized format.
    """
    if not matches_data or 'matches' not in matches_data:
        logging.error("No matches found in the API response.")
        return {}

    relevant_data = {}
    found_leagues = set()

    for match in matches_data['matches']:
        league_code = match['competition']['code']
        league_name = match['competition']['name']

        # Normalize league name
        league_name = normalize_text(league_name)

        # Get the country for the league
        country = LEAGUE_COUNTRIES.get(league_code, "Unknown")

        # Filter by league code (if needed)
        if league_code in LEAGUE_COUNTRIES:
            # Map and normalize team names
            home_team_long = map_team_name(normalize_text(match['homeTeam']['name']))
            home_team_short = map_team_name(normalize_text(match['homeTeam']['shortName']))
            away_team_long = map_team_name(normalize_text(match['awayTeam']['name']))
            away_team_short = map_team_name(normalize_text(match['awayTeam']['shortName']))

            match_info = {
                'id': match['id'],
                'league_name': league_name,
                'league_code': league_code,
                'country': country,  # Include the country
                'home_team_long': home_team_long,
                'home_team_short': home_team_short,
                'away_team_long': away_team_long,
                'away_team_short': away_team_short,
                'date': match['utcDate']
            }

            # Group matches by league
            if league_name not in relevant_data:
                relevant_data[league_name] = []
            relevant_data[league_name].append(match_info)
            found_leagues.add(league_code)
        else:
            logging.warning(f"League with code '{league_code}' is not in the allowed list.")

    # Check for missing leagues
    missing_leagues = set(LEAGUE_COUNTRIES.keys()) - found_leagues
    for league in missing_leagues:
        logging.warning(f"No matches found for league: {league}")

    return relevant_data

def step_one():
    date_input = input("Enter the date (DD/MM/YYYY): ")
    try:
        date = datetime.strptime(date_input, '%d/%m/%Y')
    except ValueError:
        logging.error("Invalid date format. Please use DD/MM/YYYY.")
        return None, None
    
    matches_data = fetch_matches_by_date(date)
    if matches_data:
        relevant_data = extract_relevant_data(matches_data)
        filename = f"matches_{date.strftime('%Y-%m-%d')}.json"
        return save_to_json(relevant_data, filename, MATCHES_FOLDER), date
    else:
        logging.error("No matches found or failed to fetch matches.")
        return None, None
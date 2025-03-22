import requests
import json
from datetime import datetime
import logging
from utils.file_utils import save_to_json
from config import API_KEY, BASE_URL, MATCHES_FOLDER

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

def extract_relevant_data(matches_data):
    relevant_data = []
    for match in matches_data['matches']:
        match_info = {
            'id': match['id'],
            'league_name': match['competition']['name'],
            'home_team_long': match['homeTeam']['name'],
            'home_team_short': match['homeTeam']['shortName'],
            'away_team_long': match['awayTeam']['name'],
            'away_team_short': match['awayTeam']['shortName'],
            'date': match['utcDate']
        }
        relevant_data.append(match_info)
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
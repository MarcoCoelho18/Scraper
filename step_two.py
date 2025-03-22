import os
import time
import logging
import json
import requests
from bs4 import BeautifulSoup
from utils.file_utils import save_game_data
from utils.validation_utils import validate_team_name
from utils.scraping_utils import construct_url, extract_general_statistics, extract_team_bet_statistics
from config import GAMES_FOLDER

def scrape_team_stats(club, game_type):
    try:
        url = construct_url(club, game_type)
        logging.info(f"Constructed URL: {url}")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logging.error(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        all_statistics = {
            "general_statistics": extract_general_statistics(soup),
            "team_bet_statistics": extract_team_bet_statistics(soup)
        }
        return all_statistics
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def step_two(json_file, date):
    with open(json_file, 'r') as f:
        matches_data = json.load(f)
    
    # Create a folder for the date
    date_folder = os.path.join(GAMES_FOLDER, date.strftime('%Y-%m-%d'))
    os.makedirs(date_folder, exist_ok=True)
    
    for match in matches_data:
        home_team = match['home_team_long']
        away_team = match['away_team_long']
        
        validated_home_team = validate_team_name(home_team)
        validated_away_team = validate_team_name(away_team)
        
        if validated_home_team and validated_away_team:
            # Create a folder for the game
            game_folder_name = f"{validated_home_team}_vs_{validated_away_team}"
            game_folder = os.path.join(date_folder, game_folder_name)
            os.makedirs(game_folder, exist_ok=True)
            
            # Save match info
            save_game_data(game_folder, match, "match_info.json")
            
            # Scrape and save home team stats
            home_stats = scrape_team_stats(validated_home_team, "home")
            if home_stats:
                save_game_data(game_folder, home_stats, f"{validated_home_team}_home_stats.json")
            time.sleep(2)
            
            # Scrape and save away team stats
            away_stats = scrape_team_stats(validated_away_team, "away")
            if away_stats:
                save_game_data(game_folder, away_stats, f"{validated_away_team}_away_stats.json")
            time.sleep(2)
        else:
            logging.error(f"Skipping game {home_team} vs {away_team} due to invalid team names.")
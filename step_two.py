import os
import time
import logging
import json
from bs4 import BeautifulSoup
from utils.file_utils import save_game_data
from utils.validation_utils import validate_team_name
from utils.scraping_utils import construct_url, extract_general_statistics, extract_team_bet_statistics, scrape_team_stats
from config import GAMES_FOLDER

def step_two(json_file, date):
    with open(json_file, 'r') as f:
        matches_data = json.load(f)
    
    date_folder = os.path.join(GAMES_FOLDER, date.strftime('%Y-%m-%d'))
    os.makedirs(date_folder, exist_ok=True)
    
    for league_name, matches in matches_data.items():
        # Create a folder for the league
        league_folder = os.path.join(date_folder, league_name.replace(' ', '_'))
        os.makedirs(league_folder, exist_ok=True)
        
        for match in matches:
            home_team = match['home_team_long']
            away_team = match['away_team_long']
            league_code = match['league_code']
            country = match['country']
            
            validated_home_team, home_country = validate_team_name(home_team, league_code)
            validated_away_team, away_country = validate_team_name(away_team, league_code)
            
            if validated_home_team and validated_away_team:
                # Create a folder for the game
                game_folder_name = f"{validated_home_team}_vs_{validated_away_team}"
                game_folder = os.path.join(league_folder, game_folder_name)
                os.makedirs(game_folder, exist_ok=True)
                
                # Save match info
                save_game_data(game_folder, match, "match_info.json")
                
                # Scrape and save home team stats
                home_stats = scrape_team_stats(validated_home_team, "home", home_country)
                if home_stats:
                    save_game_data(game_folder, home_stats, f"{validated_home_team}_home_stats.json")
                time.sleep(1)  # Reduced delay to 1 second
                
                # Scrape and save away team stats
                away_stats = scrape_team_stats(validated_away_team, "away", away_country)
                if away_stats:
                    save_game_data(game_folder, away_stats, f"{validated_away_team}_away_stats.json")
                time.sleep(1)  # Reduced delay to 1 second
            else:
                logging.error(f"Skipping game {home_team} vs {away_team} due to invalid team names.")
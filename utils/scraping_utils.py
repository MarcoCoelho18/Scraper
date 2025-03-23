import requests
from bs4 import BeautifulSoup
import logging


def construct_url(club, game_type, country):

    # Check if the competition is a UEFA competition
    
    teams_requiring_country_tag = ["Barcelona"]
    if club in teams_requiring_country_tag:
        club = f"{club} ({country})"
    # If the competition is a UEFA competition, exclude the country code
    if country == "Europe":
        club = club  # Use the club name as is, without appending the country
    else:
        club = f"{club} ({country})"  # Append the country for non-UEFA competitions
    
    # Replace spaces with %20 for URL encoding
    club = club.replace(' ', '%20')
    
    if game_type == "home":
        return f"https://www.statarea.com/team/view/{club}/host/last10"
    elif game_type == "away":
        return f"https://www.statarea.com/team/view/{club}/guest/last10"
    else:
        raise ValueError("Invalid game type. Use 'home' or 'away'.")

def extract_general_statistics(soup):
    general_statistics = {}
    general_statistics_container = soup.find('div', class_='teamstatistics')
    if general_statistics_container:
        for item in general_statistics_container.find_all('div', class_='factitem'):
            label = item.find('div', class_='label').text.strip()
            value = item.find('div', class_='value').text.strip()
            general_statistics[label] = value
    else:
        logging.warning("General statistics container not found.")
    return general_statistics

def extract_team_bet_statistics(soup):
    team_bet_statistics = {}
    team_bet_statistics_container = soup.find('div', class_='teambetstatistics')
    if team_bet_statistics_container:
        for barchart in team_bet_statistics_container.find_all('div', class_='barchart'):
            title = barchart.find('div', class_='title').text.strip()
            team_bet_statistics[title] = {}
            for barrow in barchart.find_all('div', class_='barrow'):
                name = barrow.find('div', class_='name').text.strip()
                value = barrow.find('div', class_='bar')['style'].split(':')[1].strip('%;')
                team_bet_statistics[title][name] = f"{value}%"
    else:
        logging.warning("Team bet statistics container not found.")
    return team_bet_statistics

def scrape_team_stats(club, game_type, country):
    try:
        # Construct the URL with the country
        url = construct_url(club, game_type, country)
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
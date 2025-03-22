from bs4 import BeautifulSoup
import logging

def construct_url(club, game_type):
    team_name = f"{club}"
    if game_type == "home":
        return f"https://www.statarea.com/team/view/{team_name}/host/last10"
    elif game_type == "away":
        return f"https://www.statarea.com/team/view/{team_name}/guest/last10"
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
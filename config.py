from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the API key from the environment variable
API_KEY = os.getenv("FOOTBALL_API_KEY")
if not API_KEY:
    raise ValueError("Please set the FOOTBALL_API_KEY in the .env file.")

# API base URL
BASE_URL = 'https://api.football-data.org/v4/'

# Folder paths
DATA_FOLDER = 'Data_files'
MATCHES_FOLDER = os.path.join(DATA_FOLDER, 'matches_dates')
GAMES_FOLDER = os.path.join(DATA_FOLDER, 'games')
LOGS_FOLDER = os.path.join(DATA_FOLDER, 'logs')

valid_teams = [
    # Premier League Teams
    "Liverpool", "Arsenal", "Nottingham Forest", "Chelsea", "Manchester City", "Newcastle", "Brighton", "Fulham", "Aston Villa", "Bournemouth", 
    "Brentford", "Crystal Palace", "Manchester Utd", "Tottenham", "Everton", "West Ham", "Wolves", "Ipswich", "Leicester", "Southampton", 
    # Championship Teams
    "Leeds", "Burnley", "Sheffield Utd", "Sunderland", "Coventry", "West Brom", "Bristol City", "Middlesbrough", "Blackburn", "Watford", 
    "Millwall", "Sheffield Wed", "Norwich", "Preston", "QPR", "Swansea", "Portsmouth", "Oxford United", "Hull City", "Stoke City", 
    "Cardiff", "Derby", "Luton", "Plymouth",
    # LaLiga Teams
    "Barcelona", "Real Madrid", "Atletico Madrid", "Athletic Club", "Villarreal", "Betis", "Mallorca", "Celta Vigo", "Rayo Vallecano", "Sevilla", 
    "Getafe", "Real Sociedad", "Girona", "Osasuna", "Espanyol", "Valencia", "Deportivo Alaves", "Leganes", "Las Palmas", "Valladolid", 
    # Serie A Teams
    "Inter", "Napoli", "Atalanta", "Juventus", "Lazio", "Bologna", "AC Milan", "Roma", "Fiorentina", "Udinese", 
    "Torino", "Genoa", "Como", "Verona", "Cagliari", "Lecce", "Parma", "Empoli", "Unione Venezia", "Monza", 
    # Bundesliga Teams
    "Bayern Munich", "Bayer Leverkusen", "FSV Mainz 05", "Eintracht Frankfurt", "RB Leipzig", "SC Freiburg", 
    "Borussia Monchengladbach", "VfL Wolfsburg", "FC Augsburg", "VfB Stuttgart", "Borussia Dortmund", 
    "Werder Bremen", "Union Berlin", "1899 Hoffenheim", "FC St. Pauli", "VfL Bochum", "Holstein Kiel", 
    "FC Heidenheim",
    # Ligue 1 Teams
    "Paris Saint Germain", "Marseille", "Monaco", "Nice", "Lille", "Lyon", "Strasbourg", "Lens", "Stade Brestois 29", 
    "Toulouse", "Auxerre", "Rennes", "Nantes", "Angers", "Reims", "Le Havre", "St Etienne", "Montpellier",
    # Liga Portugal Teams
    "Sporting CP", "Benfica", "FC Porto", "SC Braga", "Santa Clara", "Guimaraes", "Casa Pia", "Estoril", 
    "Famalicao", "Rio Ave", "Moreirense", "Arouca", "Nacional", "Gil Vicente", "Estrela Da Amadora", 
    "Vilafranquense", "Farense", "Boavista",
     # Eredivisie Teams
    "Ajax", "PSV", "Utrecht", "Feyenoord", "Twente", "AZ Alkmaar", "Go Ahead Eagles", "Fortuna Sittard", 
    "Groningen", "Heerenveen", "NEC Nijmegen", "NAC Breda", "Heracles", "PEC Zwolle", "Sparta Rotterdam", 
    "Willem II", "Waalwijk", "Almere City FC",
]
team_abbreviations = {
    "PSG": "Paris Saint Germain",
    "MU": "Manchester Utd",
    "MCI": "Manchester City",
    "CFC": "Chelsea",
    "ASM": "AS Monaco",
    "OL": "Olympique Lyon",
    "OM": "Olympique Marseille",
    "FCB": "FC Barcelona",
    "RM": "Real Madrid",
    "ATM": "Atletico Madrid",
    "JUV": "Juventus",
    "INT": "Inter",
    "MIL": "AC Milan",
    "BAY": "Bayern Munich",
    "BVB": "Borussia Dortmund",
    "B04": "Bayer Leverkusen",
    "S04": "Schalke 04",
    "LOSC": "Lille",
    "RBL": "RB Leipzig",
    "RMA": "Real Madrid",
    "AVS": "Vilafranquense",
    "AVES": "Vilafranquense",
    "SCP": "Sporting CP",
    "AZ": "AZ Alkmaar",
    "NEC": "NEC Nijmegen",
    "Venezia FC": "Unione Venezia",
    "FC Kaiserlautern": "Kaiserslautern",
    # Add more abbreviations as needed
}
# Dictionary of allowed leagues (league code -> league name)
ALLOWED_LEAGUES = {
    "BL1": "1. Bundesliga",
    "BL2": "2. Bundesliga",
    "BL3": "3. Bundesliga",
    "DFB": "Dfb-Cup",
    "PL": "Premier League",
    "EL1": "League One",
    "ELC": "Championship",
    "FAC": "FA-Cup",
    "SA": "Serie A",
    "SB": "Serie B",
    "PD": "Primera Division",
    "SD": "Segunda Division",
    "CDR": "Copa del Rey",
    "FL1": "Ligue 1",
    "FL2": "Ligue 2",
    "DED": "Eredivisie",
    "PPL": "Primeira Liga",
    "GSL": "Super League",
    "CL": "Champions-League",
    "EL": "UEFA-Cup",
    "EC": "European-Cup of Nations",
    "WC": "World-Cup"
}
# Dictionary of league codes to countries
LEAGUE_COUNTRIES = {
    "BL1": "Germany",
    "BL2": "Germany",
    "BL3": "Germany",
    "DFB": "Germany",
    "PL": "England",
    "EL1": "England",
    "ELC": "England",
    "FAC": "England",
    "SA": "Italy",
    "SB": "Italy",
    "PD": "Spain",
    "SD": "Spain",
    "CDR": "Spain",
    "FL1": "France",
    "FL2": "France",
    "DED": "Netherlands",
    "PPL": "Portugal",
    "GSL": "Greece",
    "CL": "Europe",
    "EL": "Europe",
    "EC": "Europe",
    "WC": "World"
}
TEAM_NAME_MAPPING = {
    "Venezia FC": "Unione Venezia",
    "Queens Park Rangers FC": "QPR",
    "Sheffield United FC": "Sheffield Utd",
    "FC Barcelona": "Barcelona",
    "Stade Rennais FC 1901": "Rennes",
    "Vitoria SC": "Guimaraes",
    "FC Bayern Munchen": "Bayern Munich",
    "RCD Espanyol de Barcelona": "Espanyol",
    "Wolverhampton Wanderers FC": "Wolves",
    # Add more mappings as needed
}

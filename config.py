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
MATCHES_FOLDER = os.path.join(DATA_FOLDER, 'matches')
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
    # LaLiga2 Teams
    "Levante", "Racing Santander", "Mirandes", "Elche", "Huesca", "Oviedo", "Almeria", "Granada CF", "Cadiz", "Cordoba", 
    "Burgos", "Deportivo La Coruna", "Sporting Gijon", "Eibar", "Castellon", "Albacete", "Malaga", "Zaragoza", "CD Eldense", "Racing De Ferrol", 
    "Tenerife", "Cartagena",
    # Serie A Teams
    "Inter", "Napoli", "Atalanta", "Juventus", "Lazio", "Bologna", "AC Milan", "Roma", "Fiorentina", "Udinese", 
    "Torino", "Genoa", "Como", "Verona", "Cagliari", "Lecce", "Parma", "Empoli", "Unione Venezia", "Monza", 
    # Serie B Teams
    "Sassuolo", "Pisa", "Spezia", "Cremonese", "Catanzaro", "Juve Stabia", "Cesena", "Bari", "SSD Palermo", "Modena", 
    "Sudtirol", "Frosinone", "Cittadella", "Carrarese", "Reggiana", "Brescia", "Sampdoria", "Mantova", "Salernitana", "Cosenza",
    # Bundesliga Teams
    "Bayern Munich", "Bayer Leverkusen", "FSV Mainz 05", "Eintracht Frankfurt", "RB Leipzig", "SC Freiburg", 
    "Borussia Monchengladbach", "VfL Wolfsburg", "FC Augsburg", "VfB Stuttgart", "Borussia Dortmund", 
    "Werder Bremen", "Union Berlin", "1899 Hoffenheim", "FC St. Pauli", "VfL Bochum", "Holstein Kiel", 
    "FC Heidenheim",
    # 2. Bundesliga Teams
    "Hamburger SV", "FC Koln", "SC Paderborn 07", "FC Kaiserslautern", "FC Magdeburg", "Hannover 96", 
    "Fortuna Dusseldorf", "SV Elversberg", "FC Nurnberg", "Karlsruher SC", "FC Schalke 04", 
    "SpVgg Greuther Furth", "SV Darmstadt 98", "Preussen Munster", "Hertha Berlin", "Eintracht Braunschweig", 
    "SSV Ulm 1846", "Jahn Regensburg",
    # Ligue 1 Teams
    "Paris Saint Germain", "Marseille", "Monaco", "Nice", "Lille", "Lyon", "Strasbourg", "Lens", "Stade Brestois 29", 
    "Toulouse", "Auxerre", "Rennes", "Nantes", "Angers", "Reims", "Le Havre", "St Etienne", "Montpellier",
    # Ligue 2 Teams
    "Lorient", "Metz", "Paris FC", "Dunkerque", "Guingamp", "Laval", "Annecy", "Bastia", "Grenoble Foot 38", 
    "Pau", "Ajaccio", "Estac Troyes", "Amiens", "Red Star FC 93", "Rodez", "Clermont Foot 63", "Martigues", "Caen",
    # Liga Portugal Teams
    "Sporting CP", "Benfica", "FC Porto", "SC Braga", "Santa Clara", "Guimaraes", "Casa Pia", "Estoril", 
    "Famalicao", "Rio Ave", "Moreirense", "Arouca", "Nacional", "Gil Vicente", "Estrela Da Amadora", 
    "Vilafranquense", "Farense", "Boavista",
    # Liga Portugal 2 Teams
    "Tondela", "Vizela", "Chaves", "Penafiel", "Alverca", "Leiria", "Torreense", "Benfica B", "Feirense", 
    "Academico Viseu", "Felgueiras", "Leixoes", "Portimonense", "Maritimo", "Pacos Ferreira", "FC Porto B", 
    "Oliveirense", "Mafra",
     # Eredivisie Teams
    "Ajax", "PSV", "Utrecht", "Feyenoord", "Twente", "AZ Alkmaar", "Go Ahead Eagles", "Fortuna Sittard", 
    "Groningen", "Heerenveen", "NEC Nijmegen", "NAC Breda", "Heracles", "PEC Zwolle", "Sparta Rotterdam", 
    "Willem II", "Waalwijk", "Almere City FC",
    # Eerste Divisie Teams
    "Volendam", "ADO Den Haag", "Excelsior", "Dordrecht", "Cambuur", "De Graafschap", "Telstar", "Emmen", 
    "Roda", "Den Bosch", "Helmond Sport", "Jong AZ", "FC Eindhoven", "MVV", "Jong Ajax", "VVV Venlo", 
    "TOP Oss", "Jong PSV", "Jong Utrecht", "Vitesse",
    # Scottish Premiership Teams
     "Celtic", "Rangers", "Hibernian", "Aberdeen", "Dundee Utd", "Hearts", "Motherwell", "St Mirren", 
    "Ross County", "Kilmarnock", "Dundee", "St Johnstone",
    # Turkish Super Lig Teams
    "Galatasaray", "Fenerbahce", "Samsunspor", "Besiktas", "Eyupspor", "Gaziantep FK", "Goztepe", 
    "Istanbul Basaksehir", "Trabzonspor", "Kasimpasa", "Rizespor", "Antalyaspor", "Konyaspor", 
    "Alanyaspor", "BB Bodrumspor", "Sivasspor", "Kayserispor", "Hatayspor", "Adana Demirspor",
    # Polish Ekstraklasa Teams
    "Rakow Czestochowa", "Jagiellonia", "Lech Poznan", "Pogon Szczecin", "Legia Warszawa", 
    "Gornik Zabrze", "Cracovia Krakow", "Motor Lublin", "GKS Katowice", "Piast Gliwice", 
    "Korona Kielce", "Radomiak Radom", "Widzew Lodz", "Puszcza Niepolomice", "Stal Mielec", 
    "Zaglebie Lubin", "Lechia Gdansk", "Slask Wroclaw"
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
    # Add more abbreviations as needed
}
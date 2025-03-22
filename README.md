# Football Data Scraper

This Python program automates the process of fetching football match data from the [Football-Data.org API](https://www.football-data.org/) and scraping team statistics from [Statarea](https://www.statarea.com/). The program organizes the data into a structured folder system for easy access and analysis.

---

## **Features**
1. **Step 1: Fetch Match Data**
   - Fetches match data for a specific date from the Football-Data.org API.
   - Saves the relevant match details (e.g., teams, league, date) to a JSON file.

2. **Step 2: Scrape Team Statistics**
   - Scrapes home and away statistics for each team in the match data from Statarea.
   - Organizes the scraped data into game-specific folders.

3. **Data Organization**
   - Creates a structured folder system:
     ```
     Data_files/
     ├── matches/                     # Match data from Step 1
     ├── games/                       # Game-specific data from Step 2
     │   ├── YYYY-MM-DD/              # Date-specific folder
     │   │   ├── Team_A_vs_Team_B/    # Game-specific folder
     │   │   │   ├── match_info.json  # Match details
     │   │   │   ├── Team_A_home_stats.json  # Home stats for Team A
     │   │   │   └── Team_B_away_stats.json  # Away stats for Team B
     └── logs/                        # Logs for debugging
     ```

---

## **Prerequisites**
Before running the program, ensure you have the following:

1. **Python 3.x** installed on your system.
2. **API Key** from [Football-Data.org](https://www.football-data.org/).
3. Required Python packages installed (see [Installation](#installation)).

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/football-data-scraper.git
   cd football-data-scraper
   ```
2. Install the required Python packages:
   ```bash
   pip install requests beautifulsoup4 python-dotenv thefuzz
   ```
3. Create a `.env` file in the root directory and add your Football-Data.org API key:
   ```
   FOOTBALL_API_KEY=your_api_key_here
   ```

---

## **Usage**
1. Run the program:
   ```bash
   python main.py
   ```
2. Enter the date in DD/MM/YYYY format when prompted:
   ```
   Enter the date (DD/MM/YYYY): 28/03/2025
   ```
3. The program will:
   - Fetch match data for the specified date.
   - Scrape team statistics for each match.
   - Save the data in the `Data_files` folder.

---

## **Folder Structure**
```
football_automation/
├── main.py                       # Entry point for the program
├── step_one.py                   # Code for Step 1: Fetching match data
├── step_two.py                   # Code for Step 2: Scraping team statistics
├── config.py                     # Configuration (API keys, constants, etc.)
├── .env                          # Environment variables (API key)
├── .gitignore                    # Excludes sensitive files from version control
└── utils/                        # Utility functions and shared code
    ├── __init__.py               # Makes utils a package
    ├── file_utils.py             # File and folder utilities
    ├── logging_utils.py          # Logging configuration
    ├── validation_utils.py       # Team name validation
    └── scraping_utils.py         # Web scraping utilities
```

---

## **Configuration**

- **API Key:** Store your Football-Data.org API key in the `.env` file:
  ```
  FOOTBALL_API_KEY=your_api_key_here
  ```
- **Team Validation:** Add valid team names and abbreviations in `config.py`:
  ```python
  valid_teams = ["Benfica", "Porto", "Gil Vicente", ...]
  team_abbreviations = {
      "BEN": "Benfica",
      "POR": "Porto",
      "GIL": "Gil Vicente",
      # Add more abbreviations as needed
  }
  ```

---

## **Logging**
The program logs its activities to the console and saves logs in the `Data_files/logs/` folder. Logs include:

- Successful data fetching and scraping.
- Errors (e.g., invalid date format, API failures).

---

## **Example Output**
After running the program for `28/03/2025`, the folder structure will look like this:
```
Data_files/
├── matches/
│   └── matches_2025-03-28.json
├── games/
│   ├── 2025-03-28/
│   │   ├── Gil_Vicente_vs_Benfica/
│   │   │   ├── match_info.json
│   │   │   ├── Gil_Vicente_home_stats.json
│   │   │   └── Benfica_away_stats.json
│   │   └── Another_Game_vs_Another_Team/
│   │       ├── match_info.json
│   │       ├── Another_Game_home_stats.json
│   │       └── Another_Team_away_stats.json
└── logs/
    └── execution_log_2025-03-28.log
```

---

## **Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgements**
- [Football-Data.org](https://www.football-data.org/) for providing the match data API.
- [Statarea](https://www.statarea.com/) for team statistics.

---

## **Contact**
For questions or feedback, please contact Your Name.


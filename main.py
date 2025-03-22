from step_one import step_one
from step_two import step_two
import logging
from utils.logging_utils import configure_logging

def main():
    # Configure logging
    configure_logging()

    # Step 1: Fetch match data and save to JSON
    json_file, date = step_one()
    
    if json_file and date:
        # Step 2: Scrape team statistics and organize by game and date
        step_two(json_file, date)
    else:
        logging.error("Step 1 failed. Step 2 will not run.")

if __name__ == "__main__":
    main()
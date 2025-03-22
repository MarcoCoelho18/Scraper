import os
import json
import logging

def save_to_json(data, filename, folder):
    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)
    
    # Save the data to the JSON file
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    logging.info(f"Data saved to {filepath}")
    return filepath

def save_game_data(game_folder, data, filename):
    try:
        # Ensure the folder exists
        os.makedirs(game_folder, exist_ok=True)
        
        # Save the data to the JSON file
        filepath = os.path.join(game_folder, filename)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data saved to {filepath}.")
    except Exception as e:
        logging.error(f"Failed to save JSON file: {e}")
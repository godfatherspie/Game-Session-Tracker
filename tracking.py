import psutil
import time
from datetime import datetime
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GAMES_FILE = os.path.join(BASE_DIR, 'games_to_track.txt')
LOG_FILE = os.path.join(BASE_DIR, 'playtime_log.txt')


def load_game_list():
    try:
        with open(GAMES_FILE, 'r') as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{GAMES_FILE} not found.")
        return []

def is_game_running(game_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == game_name:
            return True
    return False

def log_playtime(game_name, duration):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{game_name} played for {str(duration)} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def track_games():
    print("Tracking games listed in", GAMES_FILE)
    running_games = {}

    try:
        while True:
            game_list = load_game_list()

            for game in game_list:
                if is_game_running(game):
                    if game not in running_games:
                        print(f"{game} started!")
                        running_games[game] = datetime.now()
                else:
                    if game in running_games:
                        duration = datetime.now() - running_games.pop(game)
                        print(f"{game} closed. Session time: {duration}")
                        log_playtime(game, duration)

            time.sleep(5)
    except KeyboardInterrupt:
        print("Tracking stopped.")

track_games()

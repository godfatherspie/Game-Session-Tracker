import os
import sys
import time
import psutil
from datetime import datetime, timedelta

# Determine base directory
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GAMES_FILE = os.path.join(BASE_DIR, 'games_to_track.txt')
LOG_FILE = os.path.join(BASE_DIR, 'playtime_log.txt')
TOTAL_FILE = os.path.join(BASE_DIR, 'total_playtime.txt')

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

# Convert "HH:MM" to minutes
def hhmm_to_minutes(hhmm):
    hours, minutes = map(int, hhmm.split(":"))
    return hours * 60 + minutes

# Convert minutes to "HH:MM"
def minutes_to_hhmm(minutes):
    return f"{minutes // 60:02}:{minutes % 60:02}"

def load_total_playtime():
    totals = {}
    try:
        with open(TOTAL_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    name, hhmm = line.strip().split(',')
                    totals[name] = hhmm_to_minutes(hhmm)
    except FileNotFoundError:
        pass
    return totals

def save_total_playtime(totals):
    with open(TOTAL_FILE, 'w') as f:
        for game, minutes in totals.items():
            f.write(f"{game},{minutes_to_hhmm(minutes)}\n")

def log_session(game, duration):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{game} played for {duration} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def track_games():
    print("🎮 Tracking games listed in games_to_track.txt")
    running_games = {}
    total_times = load_total_playtime()

    try:
        while True:
            game_list = load_game_list()

            for game in game_list:
                if is_game_running(game):
                    if game not in running_games:
                        print(f"▶ {game} started!")
                        running_games[game] = datetime.now()
                else:
                    if game in running_games:
                        start_time = running_games.pop(game)
                        duration = datetime.now() - start_time
                        minutes = int(duration.total_seconds() // 60)

                        print(f"⏹ {game} closed. Session: {duration} (~{minutes} min)")
                        log_session(game, duration)

                        total_times[game] = total_times.get(game, 0) + minutes
                        save_total_playtime(total_times)

            time.sleep(5)
    except KeyboardInterrupt:
        print("🛑 Tracking stopped.")

track_games()

# Game-Session-Tracker


# 🕹️ Game Playtime Tracker

A lightweight, Python-based tool that tracks how long specific PC games are played by monitoring their `.exe` processes in the background. 

---

## 📦 Features

- ⏱️ Tracks runtime duration of specified game `.exe` files
- 📋 Logs each session with timestamp
- 💻 Runs as a background script or standalone `.exe` — no UI needed

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:**
  - [`psutil`](https://pypi.org/project/psutil/) — for process monitoring
  - `datetime`, `os`, `time`, `sys` — Python standard modules

---

## 📋 Prerequisites

If running the Python script directly:

1. Install [Python 3](https://www.python.org/downloads/)
2. Install required library:
   ```bash
   pip install psutil

   
## 🚀 Usage
Option 1: Run the Python Script

python tracking.py
This will start tracking all .exe names listed in games_to_track.txt.

Option 2: Run the Standalone .exe (No Python Needed)
Download game_tracker.exe from the repository.

Place it in the same folder as games_to_track.txt.

Double-click game_tracker.exe to start tracking.

Logs and total playtime will be saved in the same folder.

📌 Configuring Games
Edit games_to_track.txt and list the .exe names of games you want to monitor:

eldenring.exe
witcher3.exe
gta5.exe
Save the file — the tracker reads from it dynamically every few seconds.

📊 Outputs
playtime_log.txt: Logs sessions in the format
eldenring.exe played for 1:23:10 at 2025-06-17 19:32:01

🔒 Notes
The tool does not retroactively track past game time.

Works on any Windows machine as long as .exe and .txt files are in the same folder.

Running the .exe may trigger Windows Defender since it’s unsigned — you can ignore this if you trust your own build.

⚙️ Building the .exe (Optional)
To build your own .exe from the Python script:

bash
Copy
Edit
pip install pyinstaller
pyinstaller --onefile tracking.py
You’ll find the .exe in the dist/ folder.



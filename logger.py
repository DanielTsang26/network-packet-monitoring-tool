from datetime import datetime
from config import HISTORY_FILE
from rich.console import Console
import os
import csv

console = Console()

def log_connect(host, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    file_exists = os.path.exists(HISTORY_FILE)
    with open(HISTORY_FILE, "a") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp","Host","Status"])
        writer.writerow([timestamp,host, result])

def show_history():
    if not os.path.exists(HISTORY_FILE):
        console.print("[bold red][+] No history found.[/bold red]")
        return

    with open(HISTORY_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            console.print(f"[bold purple][{row['Timestamp']}] Host: {row['Host']} - Status: {row['Status']}[/bold purple]")
        



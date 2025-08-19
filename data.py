from rich.table import Table
from rich.console import Console
import re

console = Console()

def display_packet_summary(packet_lines):
    table = Table(title="Packet Sniffing Summary", show_lines=True, title_style="bold cyan")
    table.add_column("Protocol", style="yellow")
    table.add_column("Source", style="purple")
    table.add_column("Destination", style="purple")
    table.add_column("Info", style="blue")

    for line in packet_lines:
        parts = line.split(": ", 1)[-1].split(" / ")
        if len(parts) < 3:
            continue

        protocol = parts[2] if len(parts) > 2 else "N/A"

        # Attempt to extract source > destination from last protocol segment
        match = re.search(r"([\w.:]+) > ([\w.:]+)(.*)", parts[-1])
        if match:
            source, dest, info = match.groups()
        else:
            source, dest, info = "N/A", "N/A", parts[-1]

        table.add_row(protocol, source, dest, info.strip())

    console.print(table)
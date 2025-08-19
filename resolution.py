import socket
from rich.console import Console

console = Console()

def resolve_host(hostname):
    """this method is meant to get the host by name or by IP"""
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        console.print(f"[bold red] [+] Cannot resolve hostname {hostname} [/bold red]")
        return None

from resolution import resolve_host
from ping_processor import ping
from rich.console import Console
from args_processor import create_args_parser
from logger import show_history
from logger import log_connect
from packet_sniffer import sniff_packet_stream
import sys


console = Console()

def main():
    parse = create_args_parser()
    if len(sys.argv) == 1:
        parse.print_help()
        sys.exit(0)

    args = parse.parse_args()
    if args.history:   
        show_history()
        sys.exit(0)
    console.print(f"[bold cyan][+] Resolving host {args.target}...[/bold cyan]")
    ip_address =  resolve_host(args.target)

    if not ip_address:
        console.print(f"[bold red][+] Could not resolve host name. [/bold red]")
        return 
    
    status = ping(ip_address)
    packet_lines = []
    
    if status == "CONNECTED":
        console.print(f"[bold cyan][+] Host {args.target} ({ip_address}) is CONNECTED[/bold cyan]")
    else:
        console.print(f"[bold red][-] Host {args.target} ({ip_address}) is NOT CONNECTED[/bold red]")

    

    if args.packet:
        console.print(f"[bold green][+] Packet sniffing initiated ... captured {args.packet} packets [/bold green]")
        sniff_packet_stream(packet_count = args.packet)
    
   

    
    log_connect(args.target, status)

if __name__ =="__main__":
    main()
    


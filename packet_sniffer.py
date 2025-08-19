from rich.console import Console
from scapy.all import sniff
from data import display_packet_summary


console = Console()

def sniff_packet_stream(packet_count=10):
    packet_lines = []
    packets = sniff(count=packet_count)

    if not packets:
        console.print(f"[bold red][+] No packets found. [/bold red]")
    else:
        for packet in packets:
          summary = packet.summary()
          packet_lines.append(summary)
         
    display_packet_summary(packet_lines)

   
    
    return packets    

   


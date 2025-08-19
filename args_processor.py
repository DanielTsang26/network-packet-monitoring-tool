import argparse
from rich_argparse import RichHelpFormatter

def create_args_parser():
     parse = argparse.ArgumentParser(
        description="[bold cyan]PyPulse -- A lightweight Python tool for real-time network connectivity checks and host resolution. [/bold cyan]",
        usage="python -m ping_tool.cli --target <hostname_or_ip>[/bold cyan]",
        formatter_class=RichHelpFormatter)
     parse.add_argument("-t", "--target", help="[bold purple]Hostname or IP address[/bold purple]", required=False)
     parse.add_argument( "--history",action="store_true",help="[bold purple]Show connectivity history[/bold purple]")
     parse.add_argument("--packet", type = int, help="[bold purple] Sniff the specified number of packets and displays a table of information of the packets [/bold purple]")
    

     return parse

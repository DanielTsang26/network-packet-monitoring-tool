import subprocess
import platform 
from rich.console import Console

console = Console()


def ping(host):
    """
Returns True if host (str) responds to a ping request.
Remember that a host may not respond to a ping (ICMP) request even if 
the host name is valid.
"""
 
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf8').lower()
    if "Request timed out." in output or "100% packet loss" in output or "destination host unreachable" in output:
        return "NOT CONNECTED"
    return "CONNECTED"






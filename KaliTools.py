import subprocess
import sys
import os

# List of Kali Linux tools available via apt-get
tools = [
    "nmap", "ncat", "ndiff", "nping", "nmap-common", 
    "hydra", "dpl4hydra", "hydra-wizard", "pw-inspector", "hydra-gtk", "xhydra",
    "airbase-ng", "aircrack-ng", "airdecap-ng", "airdecloak-ng", "aireplay-ng", "airmon-ng", "airodump-ng", "airolib-ng",
    "crunch", "parsero", "theHarvester", "metasploit-framework", "msf-egghunter", "msf-exe2vba",
    "libwireshark-data", "libwireshark-dev", "tshark", "wireshark",
]

# Function to execute a shell command
def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}", file=sys.stderr)

if os.getuid() != 0:
   sys.exit("This script requires sudo privleges")

# Update package list
print("Updating package list...")
run_command(["sudo", "apt-get", "update"])

# Installs each tool
for tool in tools:
    print(f"Installing {tool}...")
    run_command(["sudo", "apt-get", "install", "-y", tool])

print("All tools installed.")

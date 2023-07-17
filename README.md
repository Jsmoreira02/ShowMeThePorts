# Show The Ports (Port Scanning)
Investigation, scanning and enumeration of open ports on target machine for pentest recognition step



`Usage: python3 ShowMeThePorts.py <options>`


**HELP OPTION:** `-h / --help`

**ENJOY!**




https://user-images.githubusercontent.com/103542430/211045595-a07b2879-9089-4dca-8d07-59659d964f23.mp4





  

# Options:

- `-t/--target` **Select target domain or IP**  
- `-lp/--LimitPort` **Limit search for ports and services**  
- `-p/--port` **Specific port to search**
- `-b/--banner` **Get the Banner (Enumeration)**
  
  
> This program must be run in the linux terminal and serves to scan and enumerate services on a target.
  REQUIRES: python3 socket module, argparse module and netcat tool 
  

**If the program does not run netcat, consider updating it with: (sudo apt-get upgrade netcat).**

**some banners may not appear with the -lp option but may appear if you only scan the desired port with the -p option**

# Pentester-journey
Investigation, scanning and enumeration of open ports on target machine for pentest recognition step



Usage: python3 ShowMeThePorts.py <options> 

HELP OPTION: -h / --help

ENJOY!









https://user-images.githubusercontent.com/103542430/211035475-4e0fcc51-76ff-4123-8524-43a529067359.mp4



![image](https://user-images.githubusercontent.com/103542430/210264499-74a2e69c-21f2-456f-8b15-81c3b7676da8.png)

  

Options:

 -----> -t/--target 
[Select target domain or IP]
  
 -----> -lp/--LimitPort 
[Limit search for ports and services]
  
 -----> -p/--port 
[Specific port to search]
  
 -----> -b/--banner
[Get the Banner (Enumeration)]
  
  
  INFO:
  This program must be run in the linux terminal and serves to scan and enumerate services on a target.
  REQUIRES: python3 socket module, argparse module and netcat tool 
  
  
  
If the program does not run netcat, consider updating it with: (sudo apt-get upgrade netcat).

some banners may not appear with the -lp option but may appear if you only scan the desired port with the -p option

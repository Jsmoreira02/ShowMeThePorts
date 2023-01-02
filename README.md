# Pentester-journey
Investigation, scanning and enumeration of open ports on target machine for pentest recognition step



Usage: python3 ShowMeThePorts.py <options>

ENJOY!









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
  
  
  
If the program does not run netcat, consider updating it with: (sudo apt-get upgrade netcat)

![Captura de tela de 2023-01-02 13-11-35](https://user-images.githubusercontent.com/103542430/210272696-62ea7af1-547c-496a-a556-2f57a45e62e4.png)

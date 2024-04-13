![Captura de tela de 2024-04-13 12-47-51](https://github.com/Jsmoreira02/ShowMeThePorts/assets/103542430/a5772e54-956b-4a38-8c9b-5f5587a878a1)


<div>
    <img src="https://img.shields.io/badge/Language%20-Rust-beige.svg" style="max-width: 100%;">
    <img src="https://img.shields.io/badge/Target OS%20-Linux, Windows-blue.svg" style="max-width: 100%;">
    <img src="https://img.shields.io/badge/Type%20-Port Scanning | Banner Grabber-darkred.svg" style="max-width: 100%;">
    <img src="https://img.shields.io/badge/Other used tools%20-Netcat,Curl-red.svg" style="max-width: 100%;">
    <img src="https://img.shields.io/badge/CYBERSECURITY%20-teste?style=flat-square style="max-width: 100%;">
</div>

# Show Me The Ports 
Rust port scanning and banner grabber for investigation, scanning and enumeration of open ports on target machine for pentest recognition step. 

> For faster results, the "curl" and "netcat" commands are used for Banner grabbing, which is used to obtain information about a computer system on a network and the services running on its open ports.

`Usage: ./ShowMeThePorts <Scope>`

`Example> ./ShowMeThePort 10.1.0.10 0-1000`

**Compiling** `rustc showMeThePorts`

![ezgif com-video-to-gif](https://github.com/Jsmoreira02/Port-Scanner/assets/103542430/042535be-3ee7-4b35-8b9a-f2b48d0088f8)

-------------------------------
  
Some banners may not appear with the banner graber option but may appear if you only scan the desired port or consider open ports and run nmap or netcat

### Remember that capturing service information is more accurate with more specialized tools such as nmap or nikto 

Good Hacking :D

use std::net::TcpStream;
use std::env::args;
use std::time::Duration;
use std::process::Command;

fn logo() -> &'static str {

    r#"

███████████████████████████████████████████████████████████████████████████████████████████
█─▄▄▄▄█─█─█─▄▄─█▄─█▀▀▀█─▄███▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─█─█▄─▄▄─███▄─▄▄─█─▄▄─█▄─▄▄▀█─▄─▄─█─▄▄▄▄█
█▄▄▄▄─█─▄─█─██─██─█─█─█─█████─█▄█─███─▄█▀█████─███─▄─██─▄█▀████─▄▄▄█─██─██─▄─▄███─███▄▄▄▄─█
▀▄▄▄▄▄▀▄▀▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀

    
    "#
}

fn get_banner(open_ports: Vec<u16>, host: &str) -> &'static str {
    
    println!("\n====================");
    println!("[+] Getting Banner");
    println!("====================\n");

    let curl_args = format!("curl -Is {} | grep -i '^Server:'", host);

    for ports in open_ports {

        let port = &ports.to_string();
        let netcat_args = vec!["-v", "-W", "2", "-w", "3", host, &port];

        if ports == 80 || ports == 8080 {

            match Command::new("sh").arg("-c").arg(&curl_args).output() {
                Ok(output) => { println!("Running now on port {} => {}", port, String::from_utf8_lossy(&output.stdout)); }
                Err(err) => {
                    println!("[!] Failed to execute process: {}", err);
                }
            }
        } 
        else {
            match Command::new("nc").args(netcat_args).output() {
                Ok(output) => { println!("Running now on port {} => {}", port, String::from_utf8_lossy(&output.stdout)); }
                Err(err) => {
                    println!("[!] Failed to execute process: {}", err);
                }
            } 
        }   
    }

    "\n[+] Banners grabed!\n"
}

fn scan_ports(host: &str, range: std::ops::RangeInclusive<u16>) -> &'static str {

    println!("============================================");
    println!("[+] Scanning the target: {}", host);
    println!("============================================\n");

    let mut open = Vec::new();

    for port in range {
        
        let timeout = Duration::from_secs(15);
        let target = format!("{}:{}", host, port);

        match TcpStream::connect(&target) {
            Ok(socket) => { 
                
                socket.set_read_timeout(Some(timeout)).expect("Failed to set read timeout");
                println!("[+] Found!: {} STATUS: OPEN!\n", port);
                open.push(port);
            }
            Err(_) => { 
                continue; 
            }
       }
    }

    println!("{}", get_banner(open, host));
    "\nExecution Finished!\n"
}

fn main(){

    let args: Vec<String> = args().collect();

    if args.len() < 3 {

        println!("Usage: ./app <IP> <Number of ports to scan>");
        println!("\nExample: ./app 192.168.14.234 0-8000 ---> It will scan 8000 ports, starting from zero");
        return;
    }

    let ip = &args[1];
    let range = &args[2]; let ports: Vec<&str> = range.split('-').collect();

    let start: u16 = match ports[0].parse() {
        Ok(num) => num,
        Err(_) => {
            println!("[X] Invalid Port Range!\n");
            return;
        }
    }; 
    
    let end: u16 = match ports[1].parse() {
        Ok(num) => num,
        Err(_) => {
            println!("[X] Invalid Port Range!\n");
            return;
        }
    };

    if end < start {

        println!("[X] Invalid port range!\n");
        return;
    }

    println!("{}", logo());
    println!("{}", scan_ports(ip, start..=end));
}

#include <iostream>
#include <fstream>
#include <SFML/Network.hpp>
#include <string>
#include <vector>

using namespace std;

bool port_scanner(string IP, int port){

    return (sf::TcpSocket().connect(IP, port) == sf::Socket::Done);
}

int banner(string IP, int port){

    sf::TcpSocket socket;
    sf::Socket::Status status = socket.connect(IP, port);

    if(status == sf::Socket::Done) {
            
        char buffer[1024];
        size_t received;                        
        string requestData = "GET / HTTP/1.1\r\nHost: " + IP + "\r\nConnection: close\r\n\r\n";

        if(port == 80){

            if(socket.send(requestData.c_str(), requestData.size()) != sf::Socket::Done){

                cout << "Error in comunicating with HTTP/HTTPS service" << endl;
                return -1;
            }

            if(socket.receive(buffer, sizeof(buffer), received) == sf::Socket::Done){

                string response(buffer, received);
                size_t server = response.find("Server:");
                
                if(server != string::npos) {

                    std::size_t endOfLine = response.find("\r\n", server);

                    if(endOfLine != string::npos) {
                
                        string serverHeader = response.substr(server, endOfLine - server);
                        cout << "Running now on port " << port << " => " << serverHeader.substr(serverHeader.find(":") + 2) << endl;
                    }
                }

                else{

                    cout << "Error in Comunicating with HTTP/HTTPS service" << endl;
                    return -1;
                }
            }
        }
        else{

            if(socket.receive(buffer, sizeof(buffer), received) == sf::Socket::Done) {
        
                string response(buffer, received);
                cout << "Running now on port " << port << " => " << response << endl;
            }
            else{
                cout << "Error in receiving service data\n" << endl;
                return -1;
            }
        }
    }
    else{
        return -1;
    }

    return 0;
}

int main(int argc, char* argv[]){

    if(argc < 3){

        cout << "\nUsage: ./app <IP or DNS> <PORT>\n" << endl;
        return -1;
    }
    else{

        ifstream logo("logo.txt");
        string show_logo;

        for(string line; getline(logo, line);){

            show_logo += line + "\n";
        }

        cout << show_logo << endl;

        string target = argv[1];
        string port_target = argv[2];

        size_t separator = port_target.find('-');
        sf::IpAddress ipAddress(target);

        if(separator == string::npos){

            cout << "============================================" << endl;
            cout << "[+] Scanning the target: " << ipAddress << " ..." << endl;
            cout << "============================================\n" << endl;

            if(port_scanner(target, stoi(port_target))){

                cout << "[+] Found!: " << port_target << " STATUS: OPEN!\n" << endl;
                cout << "====================" << endl;
                cout << "[+] Getting Banner" << endl;
                cout << "====================\n" << endl;

                banner(target, stoi(port_target));
            }

            return 0;
        }

        else{

            string start = port_target.substr(0, separator);
            string end = port_target.substr(separator + 1);
            vector<int> open_ports = {};

            int start_int = stoi(start);
            int end_int = stoi(end);

            cout << "============================================" << endl;
            cout << "[+] Scanning the target: " << ipAddress << " ..." << endl;
            cout << "============================================\n" << endl;

            for(int i = start_int; i <= end_int; i++){

                if(port_scanner(target, i)){
                    
                    cout << "[+] Found!: " << i << " STATUS: OPEN!\n" << endl;
                    open_ports.push_back(i);
                }
            }

            cout << "====================" << endl;
            cout << "[+] Getting Banner" << endl;
            cout << "====================\n" << endl;

            for(int i = 0; i <= open_ports.size(); i++){

                banner(target, open_ports[i]);
            }

            return 0;
        }
    }
    return 0;
}

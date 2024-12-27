import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m
  WELCOME TO WEB TOOL     ╔════════════════╗
 ┏━━━┓┏━━━┓┏━━┓┏━━┓┏━━━┓  ║  ERIIC TRICKER ║
 ┃┏━━┛┃┏━┓┃┗┫┣┛┗┫┣┛┃┏━┓┃  ║════════════════║
 ┃┗━━┓┃┗━┛┃━┃┃━━┃┃━┃┃━┗┛  ║  MULTY TOKEN   ║
 ┃┏━━┛┃┏┓┏┛━┃┃━━┃┃━┃┃━┏┓  ║════════════════║
 ┃┗━━┓┃┃┃┗┓┏┫┣┓┏┫┣┓┃┗━┛┃  ║ WEB TO WEB TOOL║
 ┗━━━┛┗┛┗━┛┗━━┛┗━━┛┗━━━┛  ╚════════════════╝
╔═══════════════════Note═══════════════════╗                 
║          𝐄𝐑𝐈𝐈𝐂 𝐌𝐔𝐋𝐓𝐘 𝐓𝐎𝐊𝐄𝐍 𝐖𝐄𝐁 𝐓𝐎𝐎𝐋      ║
╚══════════════════════════════════════════╝
╔══════════════════════════════════════════╗  
 \033[1;32m[√]AUTHOR    : \033[1;37m𝐄𝐑𝐈𝐈𝐂 
 \033[1;32m[√]RUL3X     : \033[1;37m𝐀𝐊 𝐎𝐅𝐅𝐋𝐈𝐍𝐄  𝐑𝐔𝐋𝐄𝐗 
 \033[1;32m[√]GITHUB    : \033[1;37m𝐄𝐑𝐈𝐈𝐂-𝐄𝐗𝐎
 \033[1;32m[√]FACEBOOK  : \033[1;37m𝐄𝐑𝐈𝐈𝐂-𝐄𝐗𝐎𝐅𝐎𝐑𝐓
 \033[1;32m[√]TOOL NAME : \033[1;37m𝐖𝐄𝐁 𝐓𝐎 𝐖𝐄𝐁
 \033[1;32m[√]VERSION   : \033[1;37m2.4
╚══════════════════════════════════════════╝
 ╔══════════════════════════════════════════╗  
 ║            𝐅𝐄𝐄𝐋 𝐓𝐇𝐄 𝐏𝐎𝐖𝐎𝐑 𝐎𝐅 𝐄𝐑𝐈𝐈𝐂       ║
 ╚══════════════════════════════════════════╝
 ╔══════════════════════════════════════════╗  
 \033[1;32m ENJOY WEB TO WEB CONVO TOOL
 \033[1;36m ERIIC TRICKER WEB TO WEB FREE TOOL""" )

def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.FACEBOOK.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message}'}
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;32m[√]MASSAGE SEND TO ERIIC TRICKER SIDE    {} of Convo\033[1;35m {} \033[1;33msent by Token {}: \n\033[1;35m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print("\033[1;32m  - Time: {}".format(current_time))
                else:
                    print("\033[1;32m[x] MESSEGE FAIL HO GYA BHOSDI KE TOKAN SAHI DAL  {} of Convo \033[1;34m{} with Token \033[1;36m{}: \n\033[1;36m{}".format(
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}'))
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)   
            print("\n\033[1;33m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;35m[!] An error occurred: {}".format(e))
def main():	
    print(logo)   
    print(' \033[1;37m [•] 3NT3R TOK3N F1L3 P4TH ➼')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;37m[•] 3NT3R TH3 GR0UP + 1NB0X U1D ➼ ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;37m[•] 3NT3R TH3 NP F1L3 P4TH ➼')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;37m[•] 3NT3R TH3 H4TT3R N4M3 ➼')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;37m[•] 3NT3R TH3 D34LY S3C0ND T1M3 ➼' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()

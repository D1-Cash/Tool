"""
MIT License

Copyright (c) 2024 Wazkza

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Made by wazkza
#DC:wazkza
#github: https://github.com/D1-Cash/Tool.git
# dm me for offers


import random
import string
import time
import threading
import requests
import sys
import uuid
import hashlib
import os

# Define ANSI escape codes for colors and styles
RESET = "\033[0m"
PURPLE = "\033[35m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

# Replace with your actual webhook URL
WEBHOOK_URL = 'https://your-webhook-url.com'

# Define the logs directory
LOGS_DIR = "logs"

# Ensure the logs directory exists
os.makedirs(LOGS_DIR, exist_ok=True)

def log_to_file(filename, message):
    # Log to a file in the logs directory
    filepath = os.path.join(LOGS_DIR, filename)
    with open(filepath, "a") as file:
        file.write(message + "\n")

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_ip_address():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def log_ip_address(ip_address):
    log_to_file("ip_addresses.txt", ip_address)

def log_password(password):
    log_to_file("passwords.txt", password)

def generate_nitro_code():
    # Generate a random Nitro-like code in the format: XXXX-XXXX-XXXX-XXXX
    segments = 4
    segment_length = 4
    nitro_code = '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=segment_length)) for _ in range(segments))
    return nitro_code

def log_nitro_code(nitro_code):
    log_to_file("nitro_codes.txt", nitro_code)

def is_valid_nitro_code(nitro_code):
    # Dummy validation function
    return random.choice([True, False])  # Simulate a 50% chance of being valid

def send_nitro_code_to_webhook(nitro_code):
    payload = {'content': f'Valid Nitro Code: {nitro_code}'}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        response.raise_for_status()
        log_to_file("webhook_log.txt", f"Sent Nitro Code to webhook: {nitro_code}")
    except requests.RequestException as e:
        log_to_file("webhook_log.txt", f"Failed to send Nitro Code to webhook: {e}")

def generate_nitro_codes_at_speed(speed_seconds=0.03):
    while True:
        nitro_code = generate_nitro_code()
        log_nitro_code(nitro_code)
        print(f"{YELLOW}Generated and logged Nitro Code: {nitro_code}{RESET}")
        
        if is_valid_nitro_code(nitro_code):
            send_nitro_code_to_webhook(nitro_code)
        
        time.sleep(speed_seconds)

def animate_coin_flip():
    frames = [
        f"{BOLD}{CYAN}  _______  \n /       \\ \n|  HEADS  |\n \\_______/ {RESET}",
        f"{BOLD}{CYAN}  _______  \n /       \\ \n|  TAILS  |\n \\_______/ {RESET}"
    ]
    for _ in range(20):  # Number of animation cycles
        for frame in frames:
            sys.stdout.write("\033[H\033[J")  # Clear screen
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\033[H\033[J")  # Clear screen after animation
    sys.stdout.write(f"{GREEN}Coin Flip Completed!{RESET}")
    sys.stdout.flush()
    time.sleep(1)

def coin_flip():
    result = "Heads" if random.choice([True, False]) else "Tails"
    return result

def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def check_website_status(url):
    try:
        response = requests.get(url)
        status_message = f"Website is reachable (Status Code: {response.status_code})" if response.status_code == 200 else f"Website returned status code {response.status_code}"
        log_to_file("website_status_log.txt", status_message)
        return status_message
    except requests.RequestException as e:
        log_to_file("website_status_log.txt", f"Failed to reach website: {e}")
        return f"Failed to reach website: {e}"

def fetch_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.status_code == 200:
            ip_info = response.json()
            log_to_file("ip_info_log.txt", str(ip_info))
            return ip_info
        else:
            log_to_file("ip_info_log.txt", f"Failed to retrieve IP info (Status Code: {response.status_code})")
            return f"Failed to retrieve IP info (Status Code: {response.status_code})"
    except requests.RequestException as e:
        log_to_file("ip_info_log.txt", f"Error fetching IP info: {e}")
        return f"Error fetching IP info: {e}"

def display_system_info():
    info = (
        f"{BOLD}{CYAN}System Information:{RESET}\n"
        f"{CYAN}OS: {os.name} ({os.uname().sysname if hasattr(os, 'uname') else 'N/A'}){RESET}\n"
        f"{CYAN}Python Version: {sys.version}{RESET}"
    )
    log_to_file("system_info_log.txt", info)
    return info

def calculate_file_hash(file_path, hash_algo='sha256'):
    hash_algorithms = {
        'md5': hashlib.md5,
        'sha1': hashlib.sha1,
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512
    }
    if hash_algo not in hash_algorithms:
        message = "Unsupported hash algorithm. Choose from: md5, sha1, sha256, sha512."
        log_to_file("file_hash_log.txt", message)
        return message

    hash_func = hash_algorithms[hash_algo]()
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hash_func.update(chunk)
        hash_value = hash_func.hexdigest()
        log_to_file("file_hash_log.txt", f"File: {file_path}, Hash ({hash_algo}): {hash_value}")
        return hash_value
    except FileNotFoundError:
        message = "File not found."
        log_to_file("file_hash_log.txt", message)
        return message
    except Exception as e:
        message = f"Error calculating hash: {e}"
        log_to_file("file_hash_log.txt", message)
        return message

def generate_random_uuid():
    uuid_value = str(uuid.uuid4())
    log_to_file("uuid_log.txt", f"Generated UUID: {uuid_value}")
    return uuid_value

def get_random_quote():
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
        "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
        "The only impossible journey is the one you never begin. - Tony Robbins",
        "Act as if what you do makes a difference. It does. - William James",
        "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
        "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
        "The best way to predict your future is to create it. - Abraham Lincoln",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Go confidently in the direction of your dreams. Live the life you have imagined. - Henry David Thoreau",
    ]
    quote = random.choice(quotes)
    log_to_file("quotes_log.txt", f"Displayed Quote: {quote}")
    return quote

grim_reaper_art = f"""
{RED}              ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#              
{RESET}
"""

def print_grim_reaper():
    print(grim_reaper_art)

def main():
    banner = f"""
{PURPLE}{BOLD}|''||''| '||              '||'       ||    .     .   '||          '||''''|  ||           
   ||     || ..     ....   ||       ...  .||.  .||.   ||    ....   ||  .   ...  .. ...   
   ||     ||' ||  .|...||  ||        ||   ||    ||    ||  .|...||  ||''|    ||   ||  ||  
   ||     ||  ||  ||       ||        ||   ||    ||    ||  ||       ||       ||   ||  ||  
  .||.   .||. ||.  '|...' .||.....| .||.  '|.'  '|.' .||.  '|...' .||.     .||. .||. ||.{RESET}
"""

    # Print the Grim Reaper art in red color
    print_grim_reaper()
    
    # Print the banner message
    sys.stdout.write(f"{banner}\n")
    
    while True:
        print(f"\n{BOLD}Choose an option:{RESET}")
        print(f"{CYAN}1. Coin Flip with Animation{RESET}")
        print(f"{CYAN}2. Generate and log a random IP address{RESET}")
        print(f"{CYAN}3. Start automatic Nitro code generation{RESET}")
        print(f"{CYAN}4. Generate and log a password{RESET}")
        print(f"{CYAN}5. Generate a random string{RESET}")
        print(f"{CYAN}6. Check website status{RESET}")
        print(f"{CYAN}7. Fetch IP address information{RESET}")
        print(f"{CYAN}8. Display system information{RESET}")
        print(f"{CYAN}9. Calculate file hash{RESET}")
        print(f"{CYAN}10. Generate random UUID{RESET}")
        print(f"{CYAN}11. Display a random motivational quote{RESET}")
        print(f"{CYAN}12. Exit{RESET}")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            animate_coin_flip()
            result = coin_flip()
            print(f"\n{YELLOW}Coin Flip Result: {result}{RESET}")
            log_to_file("coin_flip_log.txt", f"Coin Flip Result: {result}")
        elif choice == '2':
            ip_address = generate_ip_address()
            log_ip_address(ip_address)
            print(f"{YELLOW}Generated and logged IP Address: {ip_address}{RESET}")
        elif choice == '3':
            print(f"{GREEN}Starting automatic Nitro code generation at 400 WPM...{RESET}")
            # Start Nitro code generation in a separate thread
            threading.Thread(target=generate_nitro_codes_at_speed, args=(0.03,), daemon=True).start()
        elif choice == '4':
            password = generate_password()
            log_password(password)
            print(f"{YELLOW}Generated and logged Password: {password}{RESET}")
        elif choice == '5':
            random_string = generate_random_string()
            log_to_file("random_string_log.txt", f"Generated Random String: {random_string}")
            print(f"{YELLOW}Generated and logged Random String: {random_string}{RESET}")
        elif choice == '6':
            url = input("Enter the website URL to check: ")
            status = check_website_status(url)
            print(status)
        elif choice == '7':
            ip_address = input("Enter the IP address to fetch info: ")
            ip_info = fetch_ip_info(ip_address)
            print(ip_info)
        elif choice == '8':
            system_info = display_system_info()
            print(system_info)
        elif choice == '9':
            file_path = input("Enter the file path to calculate hash: ")
            hash_algo = input("Enter the hash algorithm (md5, sha1, sha256, sha512): ").strip().lower()
            file_hash = calculate_file_hash(file_path, hash_algo)
            print(f"File Hash ({hash_algo}): {file_hash}")
        elif choice == '10':
            uuid_value = generate_random_uuid()
            print(f"{YELLOW}Generated UUID: {uuid_value}{RESET}")
        elif choice == '11':
            quote = get_random_quote()
            print(f"\n{GREEN}Motivational Quote: {quote}{RESET}")
        elif choice == '12':
            print(f"{GREEN}Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid option. Please try again.{RESET}")

if __name__ == "__main__":
    main()

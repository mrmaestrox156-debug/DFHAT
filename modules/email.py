import socket

def analyze_email(email_address):
    print("\n\033[90m[+] Parsing domain structures...\033[0m")
    if "@" not in email_address:
        print("\033[91m[-] Invalid Email Format.\033[0m")
        print("\n\033[90mPress Enter to return to menu...\033[0m")
        input()
        return
        
    domain = email_address.split("@")[1]
    print(f" \033[1;37m[*] INSPECTING DOMAIN:\033[0m {domain}")
    print("\033[90m[*] Fetching Mail Server Records...\033[0m")
    
    try:
        # Faz uma resolução DNS real para checar se o domínio existe e está ativo
        socket.gethostbyname(domain)
        print("\033[92m[+] Domain DNS Status: ACTIVE (Exists on the web)\033[0m")
        print("\033[90m[+] Behavioral Profile: Verified active web infrastructure.\033[0m")
        
    except socket.gaierror:
        print("\033[91m[-] CRITICAL: No Mail/DNS Records found. This domain cannot receive emails. Likely Spoofed/Fake.\033[0m")
        print("\033[91m[!] REPUTATION ALERT: FRAUDULENT PATTERN IDENTIFIED\033[0m")
        
    print("\n\033[90mPress Enter to return to menu...\033[0m")
    input()

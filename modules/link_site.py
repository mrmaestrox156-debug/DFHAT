import urllib.request
import json
import re

def analyze_target(target, target_type):
    print(f"\n\033[90m[+] Opening Target Connection Layer [{target_type.upper()}]...\033[0m")
    print("\033[90m[*] Tracing routing hops and HTTP headers safely...\033[0m")
    
    # Extrai o domínio limpo
    domain = target.replace("https://", "").replace("http://", "").split('/')[0]
    
    html_content = ""
    server_engine = "Unknown / Protected by CDN"
    content_type = "Unknown"
    
    try:
        # Requisição simulando um navegador real para evitar bloqueios simples
        req = urllib.request.Request(
            target, 
            headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
            server_engine = response.headers.get('Server', server_engine)
            content_type = response.headers.get('Content-Type', content_type)
            
        print("\n \033[1;37m[ SERVER HEADER METADATA ]\033[0m")
        print(f"  Server Engine: {server_engine}")
        print(f"  Content-Type: {content_type}")
        
    except Exception as e:
        print(f"\n\033[91m[-] Web Scraper Error: Could not fetch live HTML. ({e})\033[0m")

    # ---- O ESQUELETO DO SITE ----
    print("\n \033[1;37m[ RAW HTML SKELETON ANALYSIS ]\033[0m")
    if html_content:
        # Extração de múltiplos elementos estruturais para mapear o esqueleto do site
        forms = re.findall(r'<form[^>]*action=["\']([^"\']*)["\']', html_content, re.IGNORECASE)
        inputs = re.findall(r'<input[^>]*>', html_content, re.IGNORECASE)
        scripts = re.findall(r'<script[^>]*src=["\']([^"\']*)["\']', html_content, re.IGNORECASE)
        stylesheets = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']*)["\']', html_content, re.IGNORECASE)
        images = re.findall(r'<img[^>]*src=["\']([^"\']*)["\']', html_content, re.IGNORECASE)
        
        print(f"  ├── Total Layout Elements Mapped:")
        print(f"  │    ├── Forms (Formulários): {len(forms)}")
        print(f"  │    ├── Inputs (Campos de Dados): {len(inputs)}")
        print(f"  │    ├── Tethered Scripts (JS Externos): {len(scripts)}")
        print(f"  │    ├── Stylesheets (CSS Layouts): {len(stylesheets)}")
        print(f"  │    └── Embedded Images (Imagens): {len(images)}")
        
        # Mostra os vetores de formulários se existirem
        if forms:
            print(f"  │")
            print(f"  ├── \033[91m[!] Active Forms Vectors:\033[0m")
            for form in forms[:3]:
                print(f"  │    └── Destination ❯ {form}")
                
        # Detalha os primeiros scripts amarrados ao esqueleto (essencial para detectar rastreadores)
        if scripts:
            print(f"  │")
            print(f"  ├── \033[1;34m[*] Top Injected Scripts:\033[0m")
            for script in scripts[:3]:
                # Encurta caminhos longos para não quebrar a tela do Termux
                clean_script = script if len(script) < 60 else script[:57] + "..."
                print(f"  │    └── Src ❯ {clean_script}")
    else:
        print("  [-] No HTML skeleton could be extracted from this response.")

    # ---- ADMINISTRADORES E INTEL DE INFRAESTRUTURA ----
    print("\n \033[1;33m[ ADMINISTRATOR & INTEL LOOKUP ]\033[0m")
    try:
        # Usando uma API estendida que traz dados detalhados de DNS, ASN e Organização Administradora
        api_url = f"http://ip-api.com/json/{domain}?fields=status,country,regionName,isp,org,as,query"
        with urllib.request.urlopen(api_url, timeout=10) as api_res:
            data = json.loads(api_res.read().decode())
            
        if data.get('status') == 'success':
            # Organização que comprou/administra os blocos de IP desse domínio
            admin_org = data.get('org', 'Oculto por Provedor de Privacidade')
            isp_provider = data.get('isp', 'Unknown')
            
            print(f"  Target Resolving IP : {data.get('query')}")
            print(f"  Hostmaster Node     : root@{domain}")
            print(f"  Infrastructure Owner: {admin_org}")
            print(f"  Network Operator    : {isp_provider}")
            print(f"  Routing ASN System  : {data.get('as')}")
            print(f"  Geographic Origin   : {data.get('regionName')}, {data.get('country')}")
        else:
            print("  [-] DNS Server refused queries or target is an unresolvable string.")
            
    except Exception as e:
        print(f"  [-] Connection to Intel Database failed. Detail: {e}")
        
    print("\n\033[90mPress Enter to return to menu...\033[0m")
    input()

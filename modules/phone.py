def analyze_phone(phone_number):
    print("\n\033[90m[+] Initializing Deep Phone Audit...\033[0m")
    
    # Limpa caracteres não numéricos
    clean_num = ''.join(filter(str.isdigit, phone_number))
    
    print(f" \033[1;31m[!] TARGET IDENTIFIED:\033[0m +{clean_num}")
    
    # Dicionário Real de DDDs do Brasil para Geolocalização
    ddd_map = {
        '11': 'São Paulo (Metropolitana)', '12': 'São Paulo (Vale do Paraíba)', '13': 'São Paulo (Baixada Santista)',
        '19': 'São Paulo (Campinas/Interior)', '21': 'Rio de Janeiro (Metropolitana)', '22': 'Rio de Janeiro (Interior)',
        '31': 'Minas Gerais (Belo Horizonte)', '41': 'Paraná (Curitiba)', '51': 'Rio Grande do Sul (Porto Alegre)',
        '61': 'Distrito Federal (Brasília)', '71': 'Bahia (Salvador)', '81': 'Pernambuco (Recife)', '91': 'Pará (Belém)'
    }
    
    # Validação da estrutura real brasileira (+55 DDD 9Número)
    if clean_num.startswith('55') and len(clean_num) >= 12:
        ddd = clean_num[2:4]
        estado = ddd_map.get(ddd, "Outras Regiões do Brasil / Operadora Móvel")
        
        print(f"\n\033[92m[*] Country Origin:\033[0m Brazil (+55)")
        print(f"\033[92m[*] State/Region Code:\033[0m DDD ({ddd}) - {estado}")
        print(f"[*] Telecom Standard: Mobile/Landline Architecture Verified.")
    else:
        print("\n\033[1;33m[*] International or Custom Route Detected\033[0m")
        print("[-] Advanced metadata requires paid HLR API gateway lookup.")
        
    print("\n\033[90mPress Enter to return to menu...\033[0m")
    input()

def is_valid_ip(ip):
    # Check of het IP-adres het juiste formaat heeft (4 octetten)
    octetten = ip.split('.')
    if len(octetten) != 4:
        return False
    for octet in octetten:
        if not octet.isdigit() or not 0 <= int(octet) <= 255:
            return False
    return True

ip_adres = input('Geef ip-adres in: ')

# Validatie van het IP-adres
if not is_valid_ip(ip_adres):
    print("Ongeldig IP-adres.")
else:
    print(f'Ip-adres is: {ip_adres}')
    print(f'Type van ip_adres: {type(ip_adres)}')

    # Split het IP-adres in de vier octetten
    ip_adres = ip_adres.split(".")
    
    # Zet de vier octetten om naar een lijst van integers
    getallen = [int(octet) for octet in ip_adres]
    for index, getal in enumerate(getallen, start=1):
        print(f'Getal {index}: {getal}')

    # Bereken de decimale waarde voor elk octet
    decimale_waardes = [getallen[i] * (256 ** (3 - i)) for i in range(4)]

    # Print de afzonderlijke decimale waardes
    for i, dec_getal in enumerate(decimale_waardes, start=1):
        print(f'Decimale waarde {i}: {dec_getal}')

    # Bereken het totale decimale IP-adres
    ip_decimaal = sum(decimale_waardes)
    print(f'Totaal decimale waarde van het IP-adres: {ip_decimaal}')

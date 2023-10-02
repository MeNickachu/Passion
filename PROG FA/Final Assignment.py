import time


def kluizen_vrij():
    with open('fa_kluizen.txt', 'r') as file:  # openen van file
        lines = file.readlines()  # lines lezen
        kluizen = len(lines)  # int maken van de lines
    kluisvrij = 12 - kluizen  # berekenen hoeveel kluisjes er vrij zijn
    if kluisvrij == 12:  # Print en return hoeveel kluisjes er nog zijn
        print('Alle kluisjes zijn vrij.')
        return kluisvrij
    elif kluisvrij >= 2:
        print(f'Er zijn {kluisvrij} kluisjes vrij.')
        return kluisvrij
    elif kluisvrij == 1:
        print('Er is 1 kluisje vrij.')
        return kluisvrij
    elif kluisvrij < 0:
        print('Error')
    else:
        print('Er zijn geen kluisjes vrij.')
    return kluisvrij


def nieuwe_kluis():
    vrijekluisjes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # lijst met alle kluisjes
    infile = open('fa_kluizen.txt', 'r+')  # variable die het .txt opend
    lines = infile.readlines()
    bezet = []  # nieuwe lijst om de bezette in te zetten
    for lijn in lines:
        rglsplit = lijn.split('; ')  # regels in de txt file splitten
        nummer = int(rglsplit[0])  # de letter aan het begin van de regel word gelezen
        bezet.append(nummer)  # hier worden de letters in de bezet list gezet
    for kluis in bezet:
        vrijekluisjes.remove(kluis)  # hier worden de bezette kluisjes uit de vrije gehaald
    if len(vrijekluisjes) > 0:  # kijk of er tenminste 1 kluis vrij is
        print(f'Er zijn nog {len(vrijekluisjes)} kluisjes vrij.')  # laat zien hoeveel kluizen nog vrij zijn
        time.sleep(1)
        wachtwoord = input('Geef een wachtwoord van minimaal 4 tekens en zonder ";" erin: ')  # wachtwoord invoeren
        if len(wachtwoord) < 4:  # controleert of het wachtwoord voldoet aan minimaal 4 tekens
            print('Wachtwoord moet minimaal 4 tekens en zonder ";" erin.')
            time.sleep(1)
            print('Probeer opnieuw.')
            time.sleep(1)
            nieuwe_kluis()  # runt de functie opnieuw zodat het wachtwoord opniew ingevoerd kan worden
        elif ';' in wachtwoord:  # controlleert of ; niet in het wachtwoord staat
            print('Wachtwoord moet minimaal 4 tekens en zonder ";" erin.')
            time.sleep(1)
            print('Probeer opnieuw.')
            time.sleep(1)
            nieuwe_kluis()
        else:
            infile.write('{}; {}\n'.format(vrijekluisjes[0], wachtwoord))
            # schrijft het nummer en het wachtwoord van het kluisje weg
            infile.close()
            print(f'Je krijgt kluisnummer {vrijekluisjes[0]}')
    else:
        print('Er zijn geen kluisjes meer over')


def kluis_openen():
    infile = open('fa_kluizen.txt', 'r+')  # variable die het .txt opend
    lines = infile.readlines()
    numkluis = int(input('Geef nummer van uw kluis: '))
    if numkluis > 12:
        print('Wij hebben kluisjes 1 t/m 12.')
        kluis_openen()
    elif numkluis < 1:
        print('Wij hebben kluisjes 1 t/m 12.')
        kluis_openen()
    else:
        for regel in lines:  # maakt een loop om alle regels in de .txt na te checken
            split = regel.strip('; ')
            nummer = int(split[0])  # maakt van het nummer in de .txt een integer
            wachtwoord = split[3:].strip('\n')  # leest het wachtwoord vanaf na de spatie tot het einde
            if nummer == numkluis:
                wwkluis = input('Geef het wachtwoord van uw kluis: ')
                if wwkluis == wachtwoord:
                    print(f'Kluisje {numkluis} is geopend.\nU kunt uw spullen er instoppen of er uit halen.')
                else:
                    print(f'Het wachtwoord {wwkluis} komt niet overeen met het echte wachtwoord van kluisje {nummer}.')
            else:
                print(f'Kluis {numkluis} is nog niet in gebruik.')


while True:
    commando = eval(input('cmd: '))
    if commando == 0:
        break
    elif commando == 1:
        kluizen_vrij()
    elif commando == 2:
        nieuwe_kluis()
    elif commando == 3:
        kluis_openen()

age = input('Geef je leeftijd: ')
try:
    ageint = int(age)
except ValueError:
    print('Invalid input. Voer asjeblieft een getal in.')
paspoort = input('Heb je een Nederlands paspoort? ')

if paspoort == 'ja':
    if ageint >= 18:
        print('Gefeliciteerd, je mag stemmen!')
    else:
        print('Helaas, je mag niet stemmen je bent te jong!')
else:
    print('Helaas, je mag niet stemmen je hebt Nederlands paspoort nodig!')

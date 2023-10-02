while True:
    aankoopprijs = float(input('Wat is de aankoop prijs van de item: '))
    verkoop = float(input('Wat is de verkoop prijs van het item: '))
    if aankoopprijs == 0:
        break
    else:
        if verkoop < 1000:
            breakeven = aankoopprijs * 1.12
            print(f'Je breakeven is €{round(breakeven, 2)} bij een aankoopprijs van €{round(aankoopprijs, 2)}!')
            winst = (verkoop/1.12) - breakeven
            if winst > 0:
                print(f'Je hebt €{round(winst, 2)} winst!')
            else:
                winst = -winst
                print(f'Je hebt €{round(winst, 2)} verlies!')
        else:
            breakeven = aankoopprijs * 1.06
            print(f'Je breakeven is €{round(breakeven, 2)} bij een aankoopprijs van €{round(aankoopprijs, 2)}!')
            winst = (verkoop / 1.06) - breakeven
            if winst > 0:
                print(f'Je hebt €{round(winst, 2)} winst!')
            else:
                winst = -winst
                print(f'Je hebt €{round(winst, 2)} verlies!')
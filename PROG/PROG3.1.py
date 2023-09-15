score = input('Geef je score: ')
scoreint = int(score)
scoreshortage = 15-scoreint
if scoreint > 15:
    print('Gefeliciteerd!')
    print('Je bent geslaagd met een score van ', scoreint, ' punten!')
elif scoreint == 15:
    print('Damnnnn bro!')
    print('Je hebt het precies gehaald met 15 punten!')
else:
    print('Helaas!')
    print('Je hebt het niet gehaald je kwam ', scoreshortage, ' punten te kort!')

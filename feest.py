#Feest luch kosten

#Benodigheden
crossaint = 17 * 0.39
stokbrood= 2 * 2.78
Kortingsbon= 3 * 0.50
prijs= (crossaint + stokbrood) - Kortingsbon 
#berekening 


prijsbakker = prijs >= 10.69
if prijsbakker:
    print ('De feestlunch kost je bij de bakker 10.69 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!’')
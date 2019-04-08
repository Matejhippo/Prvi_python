pogoj = 5

while pogoj < 10:
    print (f"Ponavljam {pogoj}")
    pogoj += 1 #pogoj = pogoj + 1
    if pogoj == 9:         #  tu rečeš, ko vrednos po preverjanju od 5 naprej doseže 9, se naredi break, to je, zaključi preverjanje
        break
print ("konec")


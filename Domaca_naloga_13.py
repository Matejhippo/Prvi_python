a = 10
b= 15
print (a)

if a > b:
    print ("Deset ni večje od petnajst!")
elif b > a:
    print ("ok")

if a < b:
    print ("Res je")

print (a / b)

string1 = "Povej, koliko si star!"
print (string1)

string2 = input ("Vpiši svojo starost: ")
print (string2 + " let, a toliko si star?")

string3 = int(input("Vpiši starost svoje mame:"))
string4 = int(input("Vpiši še starost svojega očeta: "))
print (string3 + string4)
print ("To je skupna starost tvojih staršev.")

prvo_razpolozenje = "dobro"
drugo_razpolozenje = "slabo"
razpolozenje = input("Kako si? [dobro/slabo]")
if razpolozenje == prvo_razpolozenje:
    print ("ok")
elif razpolozenje == drugo_razpolozenje:
    print ("daj no")
else:hi
    print ("pojdi se solit")

#skrivna_st = 7
#ugibanje = int(input("Ugibaj številko od 1 do 10:"))
#while ugibanje != skrivna_st:
#    ugibanje == skrivna_st

#    if ugibanje == skrivna_st:
#        print ("Bravo, uganil si, številka je 7!")
#    else:
#        print ("Poskusi še enkrat! Številka ni " + str (ugibanje) + ", kot si mislil, da je.")

prvo_stevilo = int(input("Vnesi prvo število: "))
drugo_stevilo = int(input("Vnesi drugi število: "))
funkcija1 = input("Kaj želiš, da naredim s števili; odgovori z: seštej / odštej / množi / deli.")
if funkcija1 == "seštej":
    print (prvo_stevilo + drugo_stevilo)
elif funkcija1 == "odštej":
    print (prvo_stevilo - drugo_stevilo)
elif funkcija1 == "množi":
    print (prvo_stevilo * drugo_stevilo)
elif funkcija1 == "deli":
    print(prvo_stevilo / drugo_stevilo)
else:
    print ("Gremo naprej.")
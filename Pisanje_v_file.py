#PISANJE DATOTEK V FILE : text_file je spremenljivka, in sicer predstavlja odprti fajl


# ko tole poženeš, ruzultat ni viden spodaj v RUN, pač pa glej fajn output.txt, ki se nahaja v mapi Prvi_python

# \n pomeni newline ( nova vrstica)
# \t pomeni tabulator
# \r pomeni return


file_name = "output.txt"

with open (file_name, "w") as text_file:
    text_file.write ("prva vrstica\n")
    text_file.write ("druga vrstica\n")




# če pa želiš, da se ob vskem odpiranju fajla dodaja tekst, potem namesto "w" zapišeš "a"
"""
file_name = "output.txt"

with open (file_name, "a") as text_file:
    text_file.write ("prva vrstica\n")
    text_file.write ("druga vrstica\n")
"""




# reed
with open(file_name, "r") as text_file:
    vsebina = text_file.reed()

print (vsebina)


# to je daljši način zapisa, kjer imaš funkcijo w (write), vendar moraš nujno fajl na koncu zapreti z text_file.close()
text_file = open(file_name, "r")
text_file.write ("fore\n")
text_file.close()


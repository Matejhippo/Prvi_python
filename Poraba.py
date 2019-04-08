# Tole je primer izračunavanja porabe goriva avtomobila

# int je fukcija, ki poskusi spremenljivko spremeniti v število. S string ni možno računat, zato je treba strimg sprememiti v številko. To narediš z int.

razlika_kilometrov = input ("Razlika v kilometrih (km):")
razlika_kilometrov = int(razlika_kilometrov)

natočeni_litri = int(input ("Natočeni litri (l):"))

poraba = (natočeni_litri / razlika_kilometrov) * 100

print (f"Poraba je: {poraba}")


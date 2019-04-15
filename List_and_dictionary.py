# LIST: se definira z oglatimi oklepaji {}, notri pa elemente naštevaš z vejio. Lahko vsebuje različne tipe podatkov; npr. intiger, float, pa tudi še en list


a = [1, 2, 3, 4, 5]
b = [1, 2.4, "string", [1, 2, 3, 4, 5]]

print (a[1])
print (b[-1]) #to je kompeten string iz b-ja
print (b[-1][2])

c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print (c [1:])      #pomeni, izberi od indexa ena pa do konca

print (c[:5])       #pomeni, izberi od začetka ter do petega indeksa

print (c[1:5])       #pomeni, izberi od prvega indeksa do petega indeksa

print (c[1:-2:2])       #pomeni, izberi od prvega do drugega od zadaj, ter s korakom dveh indeksom



# DICTIONARY

d = {"ključ": "vrednost",
     "ključ1": "vrednost1",
     "ključ2": "vrednost3"}

print (d)
print (d["ključ1"])         # če hošeš indeksirat en sam ključ

#dodajanje ključa

d ["nov_ključ"] = "DODATNO DODAN KLJUČ"
print (d)


e = {}
for x in range (1,10):
    e[x] = x**2
print (e)


f = "1 2 3 4 5 6 7 8 9".split (" ") # to je funkcija, da med znake dodaš npr neko ločilo
print (f)


g = " 6 7 8 9 1 2 3 4 5".split (" ")
g.sort ()               #to je funkcija, da sortiraš
print (g)


for crke in g:           # s tp funkcijo lahko zaženeš zanko, da gre vsak elemnt v svojo vrstico
    print (crke)



h = [x for x in f if int(x)%2 == 0]         #to je list comprehension
print (h)
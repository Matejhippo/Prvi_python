for x in range (1, 100):
    if x % 15 == 0:         #tukaj preverjaš, če je število deljivo s 15; % pomeni, da vrača ostanek
        print ("fizbuzz")
    elif x % 5 == 0:
        print ("fizbuzz")
    elif x % 3 == 0:
        print ("fizbuzz")
    else:
        print (x)
import random

#UPORABA MODULA Random


secret = random.randint (1, 10)
print (secret)

while True:


    secret = 5



    user_guess = int (input ("Vnesi število med 1 in 10: "))

    if user_guess < secret:
        print ("Ugibaš prenizko")

    elif user_guess > secret:
        print ("Ugibaš previsoko")

    else:
        print ("Uganil si!")
        break
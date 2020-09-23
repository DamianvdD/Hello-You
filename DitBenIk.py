print ("Hello You!")
print ("Ik ben Damian")
import time

time.sleep(1)

print ("Wie ben jij?")
print ("Typ je naam in: ")

inputnaam = input()

print ("Hallo " + inputnaam + ", Ik heb een paar vragen voor je! Laten we beginnen.") 

time.sleep(1)

print ("Zit ik op voetbal?")

time.sleep(1)

print ("A. Ja")

print ("B. Nee")

print ("C. Geen idee")

antwoord = input("typ A, B of C: ").lower()
 
if antwoord =="a":

    print ("Inderdaad ik zit op voetbal!")

elif antwoord =="b":

    print ("Nee dat klopt niet, ik hou er wel van en zit er ook zelf op.")

elif antwoord =="c":

    print ("Helaas fout, ik zit er wel op.")

else:

    print ("Je kunt alleen met A, B of C antwoorden.")

print ("Laten we naar de volgende vraag gaan!")

time.sleep(1)

print ("Waar woon ik/ben ik opgegroeit?")

time.sleep(1)

print ("A. Amsterdam")

print ("B. Zaandam")

print ("C. Haarlem")

antwoord = input("typ A, B of C: ").lower()
 
if antwoord =="a":

    print ("Nee, ik kom er wel vaak voor school.")

elif antwoord =="b":

    print ("Dat is goed! Ik ben in Zaandam opgegroeit en woon er nog steeds.")

elif antwoord =="c":

    print ("Nee, een vriend van mij woont wel in Haarlem")

else:

    print ("Je kunt alleen met A, B of C antwoorden.")

print ("Laten we naar de laatste vraag gaan!")

time.sleep(1)

print ("Hou oud ben ik?")

time.sleep(1)

print ("A. 18")

print ("B. 15")

print ("C. 16")

antwoord = input("typ A, B of C: ").lower()
 
if antwoord =="a":

    print ("Nee, ik ben 16 jaar oud. Nog 2 jaar!")

elif antwoord =="b":

    print ("Nee, helaas ik ben 16 jaar oud. Ik ben op 17-07 jarig.")

elif antwoord =="c":

    print ("Jaaaa, ik ben inderdaad 16!")

else:

    print ("Je kunt alleen met A, B of C antwoorden.")

 # .lower() maakt alles lowercase waardoor je alleen hoeft te checken voor a/b/c
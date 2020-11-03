import time

def beginverhaal():
    print("Hello You,\n")
    time.sleep(1)
    print("Beleef het verhaal van een Nieuwkomer die van een ander land naar Nederland gevlucht.\n"
      "Door bepaalde keuzes te maken kom je in Nederland terecht en krijg je de status van Mohammed of loopt het verhaal anders af.\n")
    doorgaan()

# Hier zitten alle verhaallijnen

def verhaalstukje1():
    print("Ik ben Mohammed en woon in Syrië. Ik woon in een heel arm dorp in de bergen."
          "Ik ben graag buiten en verzorg mijn moestuin met eten voor mijn familie. \n"
          "In de verte hoor ik allemaal geluiden. Wat zal ik doen?\n")
    time.sleep(2)
    print ("A. Ik blijf buiten en ga langs mijn huis lopen en kom de buurman tegen.\n")
    print ("B. Ik ren naar het huis toe.\n")
    antwoord= input("Maak een keuze, A of B? ")
    if antwoord == "A":
        verhaalstukje2()
    elif antwoord == "B":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B.")
        verhaalstukje1()


def verhaalstukje2():
    print("\nBuiten is het meestal rustig maar vandaag zijn er vreemdelingen in het dorp.\n")
    time.sleep(2)
    print("A. Ik loop langs mijn buurman en hoor hem praten en luister mee.\n")
    print("B. Ik loop naar huis toe en vraag wat er allemaal aan de hand is.\n")
    antwoord = input("Maak een keuze, A of B? ").lower()
    if antwoord == "a":
        einde1()
    elif antwoord == "b":
        verhaalstukje3()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje2()

def verhaalstukje3():
    print("\nBinnen in huis vraag ik aan mijn vrouw wat er aan de hand is.\n"
          "Ze vertelt mij dat er verandering moet komen in het les geven op school zei vind dat ook meiden naar school moeten waaronder onze dochtertjes.\n"
          "Mijn vrouw vraagt of ik een nieuw boek uit het dorp mee kan nemen als ik daar vanmiddag naar toe ga.\n")
    time.sleep(2)
    print("A. Dat boek gaat me denk ik wel lukken ik ga het drop in.\n")
    print("B. Ik ga naar de buurman toe en ga met ze in gesprek om meer te weten te komen.\n")
    antwoord = input("Maak een keuze, A of B? ").lower()
    if antwoord == "a":
        tussenzin1()
    elif antwoord == "b":
        einde1()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje3()

def tussenzin1():
    time.sleep(2)
    print("\nHier gaat het verhaal verder in het dorp en begint de reis..........\n")
    time.sleep(2)
    verhaalstukje4()

def verhaalstukje4():
    print("\nIk ben aangekomen in het drop en kom daar allemaal mensen vrolijk en blij tegen wat mij ook opvrolijkte.\n"
          "Ik ga de winkel in om het boek voor mijn dochtertjes te halen om ze nieuwe dingen te leren. Ik leg geld op de toonbank neer en dan opeens.......\n"
          "Hoor ik allemaal geluiden en hoor ik ontploffing en zie ik mensen rennen. Ik ben natuurlijk nieuwschierig en ga buiten kijken. Ik zie allemaal Taliban strijders het drop binnen stormen.\n")
    time.sleep(2)
    print("A. Ik ga terug naar binnen om te schuilen.\n")
    print("B. Ik maak dat ik hier weg kom en ren naar mijn huis toe om mijn gezin in veiligheid te brengen.\n")
    antwoord = input("Maak een keuze, A of B? ").lower()
    if antwoord == "a":
        verhaalstukje5()
    elif antwoord == "b":
        verhaalstukje6()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje4()

def verhaalstukje5():
    print("\nIk ben aangekomen in het drop en kom daar allemaal mensen vrolijk en blij tegen wat mij ook opvrolijkte.\n"
          "Ik ga de winkel in om het boek voor mijn dochtertjes te halen om ze nieuwe dingen te leren. Ik leg geld op de toonbank neer en dan opeens.......\n"
          "Hoor ik allemaal geluiden en hoor ik ontploffing en zie ik mensen rennen. Ik ben natuurlijk nieuwschierig en ga buiten kijken. Ik zie allemaal Taliban strijders het drop binnen stormen.\n")
    time.sleep(2)
    print("A. Ik ga terug naar binnen om te schuilen.\n")
    print("B. Ik maak dat ik hier weg kom en ren naar mijn huis toe om mijn gezin in veiligheid te brengen.\n")
    antwoord = input("Maak een keuze, A of B? ").lower()
    if antwoord == "a":
        verhaalstukje6()
    elif antwoord == "b":
        verhaalstukje7()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        verhaalstukje5()



# Hier zit al het overige zoals eindes en exits doorgaan

def doorgaan():
    print("A. ik wil doorgaan.")
    print("B. ik wil stoppen.\n")
    antwoord = input("Maak een keuze, A of B? ").lower()
    if antwoord == "a":
        verhaalstukje1()
    elif antwoord == "b":
        exit()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        doorgaan()

def nogeenkeer():
    print("Door jou keuzes eindigt hier het verhaal van Mohammed. Wil je het nog eens beleven door misschien andere keuzes te maken?\n")
    print("A. Ja ik wil het nog eens doen.")
    print("B. Nee ik wil stoppen.\n")
    antwoord = input("Maak een keuze, A of B? ").lower()
    if antwoord == "a":
        verhaalstukje1()
    elif antwoord == "b":
        exit()
    else:
        print("Je kunt alleen antwoorden met A of B ")
        nogeenkeer()

def einde1():
    print("Mijn buurman is druk in gesprek met de vreemdelingen die waarschijlijk aanhangers van de Taliban zijn.\n"
          "Ze zeggen dat ik gezocht wordt omdat ik mijn dochters naar school wil laten gaan wat een strafbaar feit is.\n"
          "Ik wordt opgepakt. Helaas zit ik nog steeds gevangen en wacht af wat er met mij gaat gebeuren.\n")
    nogeenkeer()


beginverhaal()

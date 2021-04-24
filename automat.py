seznam_zbozi = {'redbull' : '50' , 'bigshock' : '45', 'monster' : '38' ,'crazywolf' : '15'} #seznam a cena zboží, které automat nabízí
seznam_minci = ('1' , '2' , '5' , '10' , '20' , '50') #povolené mince
cena = 0 
vratit = 0
vydej = ""
zbozi = ""


def volba_zbozi(): #definování funkce na výběr zboží
    global cena #globální proto, aby mohly ostatní funkce používat 
    global zbozi
    zbozi_vybrano = False #nastavení proměné, díky které budu moct vystoupit z while cyklu
    while zbozi_vybrano == False: #nastavení podmínky
        zbozi = input() #uživatel zadá požadované zboží
        if zbozi in seznam_zbozi: #kontrola zboží (jestli je dostupné)
            zbozi_vybrano = True #ukončení cyklu
            cena = int(seznam_zbozi[zbozi]) #zjištění ceny zboží pomocí slovníku
            print("Vybrali jste: " + zbozi) 
        else: #pokud se zboží nenachází v seznamu zboží, program vypíše 'chybu'
            print("Produkt neexistuje")

def platba_kartou(cena): #definování funkce pro platbu kartou
    print('Automat strhnul z karty: ' + str(cena) + 'Kč') #odpověď + je potřeba převést cenu do stringu / textu

def platba_cash(cena): #definice funkce pro platbu cash / mincí
    kredit = 0 #začínáme na nule, abychom mohli sčítat vhozené mince
    vratit = 0 #nadefinování proměnné pro pozdější využití, výpočtu vrácení 
    while int(kredit) < int(cena): #podmínka: pokud kredit je < cena zboží (obojí převádím na číslo, aby se mohlo počítat)
        print('Prosím vhoďte minci: ')
        vhozena_mince = input() #uživatel vhodí minci
        if str(vhozena_mince) in seznam_minci: #kontrola vhozené mince podle seznamu povolených mincí
            kredit = kredit + int(vhozena_mince) #spočítání kreditu 
            print('kredit: ' + str(kredit)) #vyhození celkového kreditu
        else:
            print('Takova mince neexistuje') #při vhození neexistující mince se zobrazí chybová hláška
        vratit = int(kredit) - int(cena) #vypočítání, kolik mincí má automat vrátit
    print('Automat vrací: ' + str(vratit)) #vypsání kolik mincí automat vrátí

def platba(): #definování funkce platby
    platba = '' #prázdná lokální proměnná
    while platba != 'mince' or 'karta': #dokud není zvolena platba mincí nebo kartou cyklus se opakuje
        print('Zvolte způsob platby: (mince nebo karta)')
        platba = input()
        if platba == 'karta':
            print("Zvolili jste platbu kartou.")
            platba_kartou(cena) #načítám předem definovanou funkci
            break
        elif platba == 'mince':
            print("Zvolili jste platbu mincemi")
            print("Zaplaťte: " + str(cena) + "Kč")
            platba_cash(cena)
            break
        else:
            print('Toto není validní způsob platby') #pokud není zvolen jeden z povolenných způsobů platby, vypiš chybu

while True: #dokud je pravda - nekonečný cyklus, ve kterém běží program
    print(25 * "_") #formátování
    print('Zvolte zboží: ') 
    for i in seznam_zbozi: #vytvoření vizuálu, aby program vypsal zboží ze slovníku s jejich cenou
        print(i + " " + seznam_zbozi[i] + "Kč") 
    print(25 * "_") #formátování 2
    volba_zbozi() #použití funkce k volbě zboží
    platba() #použití funkce k platbám
    print('Automat vydává zboží: ' + zbozi)
    print("Děkujeme za nákup!") #ukončení relace s 1 zákazníkem a začátek s novým

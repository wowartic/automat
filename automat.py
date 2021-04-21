
seznam_zbozi = {'redbull' : '50' , 'monster' : '38' , 'bigshock' : '45'}
seznam_minci = ('1' , '2' , '5' , '10' , '20' , '50')
cena = 0
vratit = 0
vydej = ""
zbozi = ""


def volba_zbozi():
    global cena
    global zbozi
    zbozi_vybrano = False
    while zbozi_vybrano == False:
        zbozi = input()
        if zbozi in seznam_zbozi:
            zbozi_vybrano = True
            cena = int(seznam_zbozi[zbozi])
            print("vybraljbkcd " + zbozi)
        else:
            print("neiiininini")

def platba_kartou(cena):
    print('automat si strhnul z karty: ' + str(cena) + 'kc')

def platba_cash(cena):
    kredit = 0
    vratit = 0
    while int(kredit) <= int(cena):
        print('prosim vhodte minci: ')
        vhozena_mince = input()
        if str(vhozena_mince) in seznam_minci:
            kredit = kredit + int(vhozena_mince)
            print('kredit: ' + str(kredit))
        else:
            print('takova mince neexistuje')
        vratit = int(kredit) - int(cena)
    print('automat vraci: ' + str(vratit))

def platba():
    platba = ''
    while platba != 'mince' or 'karta':
        print('zvolte zpusob platby: (mince nebo karta)')
        platba = input()
        if platba == 'karta':
            print("zvolili jste platbu kartou")
            platba_kartou(cena)
            break
        elif platba == 'mince':
            print("zvolili jste platbu mincemi")
            print("zaplatte: " + str(cena) + "kc")
            platba_cash(cena)
            break
        else:
            print('toto neni validni zpusob platby:')

while True:
    print('zvolte zbozi')
    print(seznam_zbozi)

    volba_zbozi()
    platba()
#    vratit = int(kredit) - int(cena)
#    print('automat vraci: ' + str(vratit))
    print('automat vydava zbozi: ' + zbozi)

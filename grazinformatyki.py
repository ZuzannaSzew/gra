import random

def rozpocznij_gre():
    imie_gracza = input("podaj imię gracza: ")
    gracz = {
        'imie': imie_gracza,
        'zdrowie': 100,
        'atak': 20,
        'obrona': 10,
        'doswiadczenie': 0,
        'poziom': 1,
        'ekwipunek': {'Zdrowie Potion': 2, 'Mikstura Ataku': 1},
        'zloto': 0,
        'umiejetnosci_specjalne': ['Ognisty Atak', 'Skok Niedźwiedzia']
    }
    print("")
    print(f"Witaj, {gracz['imie']}! Rozpoczynasz swoją przygodę.")

    while True:
        if not wybor_gracz(gracz):
            break

rozpocznij_gre()



#wybór gracza z lub p
def wybor_gracz(gracz):

    print("")
    print(f"{gracz['imie']} Zacznijmy od wyboru gracza.")
    print("Jakim graczem chcesz grać?")
    print("1. Gracz początkujący")
    print("2. Gracz zaawansowany")
    print("3. Sam nie wiem:))")
 
    wybor = input("Wprowadź numer opcji: ")
    if  wybor == '1':
            print("Wybrałeś gracza początkującego:)")
            return wybor_labirynt_p(gracz)
    
    elif  wybor == '2':
            print("Wybrałeś gracza zaawansowanego")
            return wybor_labirynt_z(gracz)
    
    elif  wybor == '3':
            print("W takim razie musisz jeszcze się zastanowić i jak już będzie dezyzja to zapraszamy do gry:))" )
            return True
    else:
            print("Nieprawidłowy wybór")
            print("Spróbuj jeszcze raz")
            return True



#wybór drogi w labiryncie
def wybor_labirynt_p(gracz):
        print("")
        print("Przechodzisz przez labirynt...")
        print("1. Skręć w lewo.")
        print("2. Skręć w prawo.")
        print("3. Idź prosto.")
        print("4. Idź do sklepu.")
        print("5. Spotkaj postać niezależną.")
        print("6. Przeszukaj lokację.")
        print("7. Zakończ grę.")

        wybor = input("Wprowadź numer opcji: ")

        if wybor == '1':
            print("Spotykasz potwora!")
            potwor = {'imie': 'Potwór', 'zdrowie': 30, 'atak': 15, 'obrona': 5, 'umiejetnosci_specjalne': ['Szybki Atak', 'Odbicie Ciosu']}
            return potwor_walka(gracz, potwor)
    
    
        elif wybor == '2':
            print("Nic się nie dzieje. Kontynuujesz drogę.")
            return wybor_labirynt_p(gracz)

        elif wybor == '3':
            print("Znajdujesz skarb! Gratulacje!")
            zdobadz_doswiadczenie(gracz['doswiadczenie'], 100, gracz['poziom'], gracz['atak'], gracz['obrona'], gracz['zdrowie'])
            return True

        elif wybor == '4':
            handel(gracz['ekwipunek'], gracz['zloto'])

        elif wybor == '5':
            postac_niezalezna = {'imie': 'Przyjazna Postać', 'rozmowa': 'Cześć! Życzę ci powodzenia'}
            interakcja_z_postacia(gracz, postac_niezalezna)
            return True

        elif wybor == '6':
            lokacja = {'nazwa': 'Stary Las', 'opis': 'Gęsty las pełen tajemnic.'}
            lokacja_opisz_lokacje(lokacja['nazwa'], lokacja['opis'])
            lokacja_przeszukaj_lokacje(gracz['ekwipunek'], gracz)
            return True

        elif wybor == '7':
            print("Zakończono grę. Dziękujemy za grę!")
            return False

        else:
            print("Nieprawidłowy wybór")
            print("Spróbuj jeszcze raz")
            print(".................." )
            return wybor_labirynt_p(gracz)

    
def wybor_labirynt_z(gracz):      
        print("")
        print("Przechodzisz przez labirynt...")
        print("1. Zakończ grę.")
        print("2. Przeszukaj lokację.")
        print("3. Spotkaj postać niezależną.")
        print("4. Idź do sklepu.")
        print("5. Idź prosto.")
        print("6. Skręć w prawo.")
        print("7. Skręć w lewo.")
          
        wybor = input("Wprowadź numer opcji: ")

        if wybor == '1':
            print("Zakończono grę. Dziękujemy za grę!")
            return False

        elif wybor == '2':
            lokacja = {'nazwa': 'Stary Las', 'opis': 'Gęsty las pełen tajemnic.'}
            lokacja_opisz_lokacje(lokacja['nazwa'], lokacja['opis'])
            lokacja_przeszukaj_lokacje(gracz['ekwipunek'], gracz)
            return True
        
        elif wybor == '3':
            postac_niezalezna = {'imie': 'Przyjazna Postać', 'rozmowa': 'Cześć! Życzę ci powodzenia'}
            interakcja_z_postacia(gracz, postac_niezalezna)
            return True
        
        elif wybor == '4':
            handel(gracz['ekwipunek'], gracz['zloto'])
        
        elif wybor == '5':
            print("Znajdujesz skarb! Gratulacje!")
            zdobadz_doswiadczenie(gracz['doswiadczenie'], 100, gracz['poziom'], gracz['atak'], gracz['obrona'], gracz['zdrowie'])
            return True    

        elif wybor == '6':
            print("Spotykasz potwora!")
            potwor = {'imie': 'Potwór', 'zdrowie': 30, 'atak': 15, 'obrona': 5, 'umiejetnosci_specjalne': ['Szybki Atak', 'Odbicie Ciosu']}
            return potwor_walka(gracz, potwor)
     
  
        elif wybor == '7':
            print("Nic się nie dzieje. Kontynuujesz drogę.")
            return wybor_labirynt_z(gracz)

        else:
            print("Nieprawidłowy wybór.")

        return wybor_labirynt_z(gracz)



def atakuj(atak):
    return random.randint(1, atak)


def otrzymaj_obrazenia(zdrowie, obrazenia, obrona):
    zdrowie -= max(0, obrazenia - obrona)
    return zdrowie


def leczenie(ekwipunek, zdrowie):
    if 'Zdrowie Potion' in ekwipunek and ekwipunek['Zdrowie Potion'] > 0:
        print("Używasz Zdrowie Potion.")
        zdrowie += random.randint(20, 30)
        ekwipunek['Zdrowie Potion'] -= 1
        print(f"Odzyskujesz zdrowie. Aktualne zdrowie: {zdrowie}")
    else:
        print("Nie masz Zdrowie Potion w ekwipunku.")


def uzyj_miksture_ataku(ekwipunek, atak):
    if 'Mikstura Ataku' in ekwipunek and ekwipunek['Mikstura Ataku'] > 0:
        print("Używasz Mikstura Ataku.")
        atak += random.randint(5, 10)
        ekwipunek['Mikstura Ataku'] -= 1
        print(f"Atak zostaje zwiększony. Aktualny atak: {atak}")
    else:
        print("Nie masz Mikstura Ataku w ekwipunku.")


def zdobadz_doswiadczenie(doswiadczenie, punkty, poziom, atak, obrona, zdrowie):
    doswiadczenie += punkty
    print(f"Zdobyłeś {punkty} punktów doświadczenia. Aktualne doświadczenie: {doswiadczenie}")
    if doswiadczenie >= poziom * 100:
        poziom_up(poziom, atak, obrona, zdrowie)


def poziom_up(poziom, atak, obrona, zdrowie):
    poziom += 1
    atak += 5
    obrona += 3
    zdrowie += 20
    doswiadczenie = 0
    print(f"Awansujesz na poziom {poziom}! Nowe statystyki: Zdrowie {zdrowie}, Atak {atak}, Obrona {obrona}")
    return poziom, atak, obrona, zdrowie, doswiadczenie


def handel(ekwipunek, zloto):
    print("Przechodzisz do sklepu.")
    print("Co chcesz zrobić?")
    print("1. Kup zdrowie potion (10 złota)")
    print("2. Kup miksturę ataku (15 złota)")
    print("3. Kup Magiczną Miksturę (25 złota)")
    print("4. Kup Tarczę Ognioodporną (30 złota)")
    print("5. Wyjdź ze sklepu")

    wybor = input("Wprowadź numer opcji: ")

    if wybor == '1':
        kup_przedmiot(ekwipunek, 'Zdrowie Potion', 10)
    elif wybor == '2':
        kup_przedmiot(ekwipunek, 'Mikstura Ataku', 15)
    elif wybor == '3':
        kup_przedmiot(ekwipunek, 'Magiczna Mikstura', 25)
    elif wybor == '4':
        kup_przedmiot(ekwipunek, 'Tarcza Ognioodporna', 30)
    elif wybor == '5':
        print("Wychodzisz ze sklepu.")




def uzyj_umiejetnosci(umiejetnosci_specjalne):
    print("Posiadasz umiejętności specjalne:")
    for i, umiejetnosc in enumerate(umiejetnosci_specjalne, start=1):
        print(f"{i}. {umiejetnosc}")

    wybor = input("Wybierz numer umiejętności do użycia (0 aby wrócić): ")

    if wybor.isdigit():
        wybor = int(wybor)
        if 0 < wybor <= len(umiejetnosci_specjalne):
            print(f"Używasz {umiejetnosci_specjalne[wybor - 1]}!")
        elif wybor == 0:
            print("Powrót do menu.")
        else:
            print("Nieprawidłowy wybór.")
    else:
        print("Nieprawidłowy wybór.")




def postac_niezalezna_rozmowa(postac):
    print(f"{postac['imie']}: {postac['rozmowa']}")

def interakcja_z_postacia(gracz, postac):
    print(f"{gracz['imie']} spotyka postać niezależną - {postac['imie']}.")
    postac_niezalezna_rozmowa(postac)



#potwor
def potwor_atakuj(atak):
    return random.randint(1, atak)

def potwor_otrzymaj_obrazenia(zdrowie, obrazenia, obrona):
    zdrowie -= max(0, obrazenia - obrona)
    return zdrowie

def potwor_uzyj_umiejetnosci_specjalnej(umiejetnosci_specjalne):
    umiejetnosc = random.choice(umiejetnosci_specjalne)
    print(f"Używasz umiejętności specjalnej: {umiejetnosc}")

def potwor_walka(gracz, potwor):
    print(f"Spotykasz potwora - {potwor['imie']}!")

    while gracz['zdrowie'] > 0 and potwor['zdrowie'] > 0:
        print(f"{gracz['imie']} zdrowie: {gracz['zdrowie']} | {potwor['imie']} zdrowie: {potwor['zdrowie']}")
        print("1. Atakuj")
        print("2. Uciekaj")
        print("3. Leczenie")
        print("4. Użyj Mikstury Ataku")
        print("5. Użyj Umiejętności Specjalnej")

        akcja = input("Wybierz akcję: ")

        if akcja == '1':
            obrazenia_gracza = atakuj(gracz['atak'])
            obrazenia_potwora = potwor_atakuj(potwor['atak'])

            print("")
            print(f"{gracz['imie']} zadaje {obrazenia_gracza} obrażeń.")
            potwor['zdrowie'] = potwor_otrzymaj_obrazenia(potwor['zdrowie'], obrazenia_gracza, potwor['obrona'])

            print(f"{potwor['imie']} zadaje {obrazenia_potwora} obrażeń.")
            gracz['zdrowie'] = otrzymaj_obrazenia(gracz['zdrowie'], obrazenia_potwora, gracz['obrona'])

        elif akcja == '2':
            print("")
            print("Uciekasz z walki.")
            return False

        elif akcja == '3':
            print("")
            leczenie(gracz['ekwipunek'], gracz['zdrowie'])

        elif akcja == '4':
            print("")
            uzyj_miksture_ataku(gracz['ekwipunek'], gracz['atak'])

        elif akcja == '5':
            print("")
            potwor_uzyj_umiejetnosci_specjalnej(potwor['umiejetnosci_specjalne'])

    if gracz['zdrowie'] <= 0:
        print("")
        print(f"{gracz['imie']} został pokonany. Koniec gry.")
        return False
    else:
        print("")
        print(f"{potwor['imie']} został pokonany. Gratulacje!")
        zdobadz_doswiadczenie(gracz['doswiadczenie'], 50, gracz['poziom'], gracz['atak'], gracz['obrona'], gracz['zdrowie'])
        return True




def kup_przedmiot(ekwipunek, przedmiot, cena):
    if gracz['zloto'] >= cena:
        ekwipunek[przedmiot] += 1
        gracz['zloto'] -= cena
        print(f"{gracz['imie']} kupuje {przedmiot}. Aktualne złoto: {gracz['zloto']}")
    else:
        print("Nie masz wystarczająco złota.")

def lokacja_opisz_lokacje(nazwa, opis):
    print(f"Jesteś w {nazwa}. {opis}")

def lokacja_przeszukaj_lokacje(ekwipunek, gracz):
    print(f"{gracz['imie']} przeszukuje lokację...")
    losowa_szansa = random.randint(1, 10)
    if losowa_szansa > 5:
        print("Znalazłeś ukryty skarb!")
        zdobadz_doswiadczenie(gracz['doswiadczenie'], 50, gracz['poziom'], gracz['atak'], gracz['obrona'], gracz['zdrowie'])
    else:
        print("Nie znalazłeś nic wartościowego.")

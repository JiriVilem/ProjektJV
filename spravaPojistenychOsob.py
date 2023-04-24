import sys
from .pojistenaOsoba import PojistenaOsoba

class SpravaPojistenychOsob:

    def __init__(self):
        self.seznamPojistenych: dict[str, list[PojistenaOsoba]] = {}

        self._menuVolby = {
            '1' : self.addNew,
            '2' : self.search,
            '3' : self.printAll,
            '4' : self.exit
            }
        
    def menu(self): 
        print("Zvolte možnost:\n1 - přidat pojištěného\n2 - vyhledat pojištěného\n3 - vypsat seznam pojištěných\n4 - ukončit program\n")

    def checkInput(self, vstup: str): 
        if  vstup not in self._menuVolby:
            print('Chybný vstup')
            return -1
        
        return vstup

    def addNew(self): 
        
        jmeno = input('Jméno: ')
        prijmeni = input('Příjmení: ')
        vek = input('Věk: ')
        telefon = input('Telefon: ')

        try:
            osoba = PojistenaOsoba(jmeno=jmeno, prijmeni=prijmeni, vek=int(vek), telefon=telefon)
        except:
            print('Chybné hodnoty')
            self.addNew()

        if f'{osoba.jmeno}_{osoba.prijmeni}' in self.seznamPojistenych:
            self.seznamPojistenych[f'{osoba.jmeno}_{osoba.prijmeni}'].append(osoba)
        else:
            self.seznamPojistenych[f'{osoba.jmeno}_{osoba.prijmeni}'] = [osoba]

    def printAll(self): 
        for osoby in  self.seznamPojistenych.values():
            for osoba in osoby:
                print(osoba)

    def search(self): 
        jmeno = input('Jméno: ')
        prijmeni = input('Příjmení: ')
        osoby = self.seznamPojistenych.get(f'{jmeno}_{prijmeni}', [])

        print()
        if osoby:
            for osoba in osoby:
                print(osoba)
        else:
            print('Nenalezen')

    def exit(self): 
        print('Děkujeme, že používáte náš seznam pojistných.')
        sys.exit()

    def mainloop(self): 
        print('------------------------')
        print('Evidence pojištěných')
        print('------------------------')

        while True:
            self.menu()
            vstup = input('>> ')
            vstup = self.checkInput(vstup)

            if vstup == -1:
                continue

            print('\n')
            self._menuVolby[vstup]()
            print('')
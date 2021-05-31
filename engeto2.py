MESTA = ('Praha', 'Viden','Olomouc','Svitavy','Zlin','Ostrava')
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = '=' * 40
SLEVY = ('Olomouc','Ostrava')
AKTUALNI_ROK = 2021
print(ODDELOVAC)
print('Vytejte v nasi aplikaci.')
print(ODDELOVAC) #pouzijeme viceradkovy string
print('''
1 - Praha   | 150 
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
''')
print(ODDELOVAC)
por_cislo = int(input("Vyber cislo lokality: "))
if por_cislo < 1 or por_cislo > 6:
  print("Vami vybrane cislo neni v nabidce, ukoncuji")
else:
    index = por_cislo - 1
    destinace = MESTA[index]
    cena = CENY
    print("Destinace:", destinace)
    print(ODDELOVAC)
zadene_mesto = input("Zadej jmeno mesta: ")
if zadene_mesto in MESTA:
  index = MESTA.index(zadene_mesto)
  destinace = MESTA[index]
  cena = CENY[index]
  #print("Destinace: ", destinace)
  #print("Destinace: " + destinace)
  print(f"Destinace: {destinace}")
  print(ODDELOVAC)
else:
  print("Do takoveho mesta nejezdime!")
  exit()
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")

if jmeno.isalpha() and prijmeni.isalpha():
  print(f"JMENO: {jmeno}, PRIJMENI: {prijmeni}")
  print(ODDELOVAC)
rok_narozeni = int(input("Zadej rok narozeni: "))
vek = AKTUALNI_ROK - rok_narozeni 

if vek >= 18:
  print("Pokracuj...")
  print(ODDELOVAC)
else:
  print("Nase sluzby jsou jen pro osoby strasi 18 let.")
  exit()
  mail = input("Zadej mail: ")
mail = input("Zadej mail: ")
if "@" in mail and "." in mail:
  print("Ok")
else:
  print("Spatny mail")
heslo = input('Zadej heslo:')
if len(heslo) >= 8 and not heslo.isalpha() and not heslo.isnumeric():
  print("Vse je ok")
else:
  print("Hesle musi mist aspon 8 znaku a nesmi byt tvoreno jen z cisel a pismen")
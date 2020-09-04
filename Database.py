import sqlite3
import datetime
datetime.date.fromisoformat('2019-12-04')
#Her oprettes en forbindelse til databasefilen
#Hvis filen ikke findes, vil sqlite oprette en ny tom database.
con = sqlite3.connect('data_maleri.db')
print('Database åbnet')

try:
    con.execute("""CREATE TABLE produkter (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		navn STRING,
        pris INTEGER)""")
    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')

try:
    con.execute("""CREATE TABLE ordre (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		produkt INTEGER,
        dato INTEGER,
        status INTEGER)""")
    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')

try:
    con.execute("""CREATE TABLE fremstilling (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		robot INTEGER,
        ordrenummer INTEGER)""")
    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')

try:
    con.execute("""CREATE TABLE status (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		status STRING)""")
    print('Tabel oprettet')
except Exception as e:
    print('Tabellen findes allerede')



c = con.cursor()
#c.execute('INSERT INTO personer (navn,alder,land) VALUES (?,?,?)', ("Hans", 38, 1))
#c.execute('INSERT INTO produkter (navn,pris) VALUES (?,?)', ("DeadPool", 900))
#c.execute('INSERT INTO status (status) VALUES (?)', ("Afsendt",))
#c.execute('DROP TABLE produkter')
#c.execute('DELETE FROM status WHERE status.id =5')
#Efter at have ændret i databasen skal man kalde funktionen commit.
con.commit()

#Denne variabel bruges til at modtage input fra brugeren
inp = ''

print('')
print('Kommandoer: ')
print('  vis - Viser alle status i databasen')
print('  visp - Viser alle produkter')
print('  viso - Viser alle ordre')
print('  lavordre - Laver ny ordre')
print('  q   - Afslut program')


while not inp.startswith('q'):
    inp = input('> ')

    if inp == 'vis':
        c = con.cursor()
        c.execute('SELECT id, status FROM status')

        for p in c:
            print('id: {} er {} '.format(p[0], p[1]))

    elif inp == 'visp':
        c = con.cursor()
        c.execute('SELECT navn, pris FROM produkter')

        for p in c:
            print('Produkt: {} Pris: {} '.format(p[0], p[1]))

    elif inp == 'viso':
        c = con.cursor()
        c.execute('SELECT produkt, dato, status FROM ordre')

        for p in c:
            print('Produkt: {} er bestilt den {} status: {} '.format(p[0], p[1], p[2]))
        con.commit()

    elif inp == 'lavordre':
        n = input('Vælg produkt: ');
        x = datetime.datetime.now()
        #print(x)
        #print(x.strftime("%A")) hvilken dag   #print(x.year) hvilket år
        #print(x.strftime("%d"),"-",x.strftime("%m"),"-",x.strftime("%Y")) #dansk dato
        print( x.strftime('We are the %d, %b %Y'))

        c.execute('INSERT INTO ordre (produkt,dato,status) VALUES (?,?,?)', (n,x,1))
        con.commit()

import sqlite3 as dbapi

print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)
try:
    bbdd = dbapi.connect('bbdd.dat')
except(dbapi.DatabaseError):
    print("Erro na BD")
else:
    print("Conectado á BD")
    print(bbdd)

try:
    c = bbdd.cursor()

    c.execute('''create table usuarios (dni text,
                                        nome text,
                                        direccion text)''')

    c.execute('''insert into usuarios values ('3333-A', 'Maria', 'Canceleiro') ''')

    c.execute('''insert into usuarios values ('4444-B', 'Manuel', 'Rosalia') ''')

    c.execute('''insert into usuarios values ('5555-C', 'Ana', 'Areal') ''')

    bbdd.commit()

except dbapi.DatabaseError as e:
    print("Erro na BD " + str(e))

try:
    c.execute('''select dni, nome, direccion from usuarios''')

    print(type(c.fetchall()))
    for rexistro in c.fetchall():
        print("Nome: " + rexistro[1])

except dbapi.DatabaseError as e:
    print("Erro na BD " +  str(e))

try:
    """Non Facer ASÍ!!!
    dni=input("Introduce o dni: ")
    c.execute('''select dni, nome, direccion from usuarios where dni="'''+ dni + '"')"""


    dni = input("Introduce o dni: ")
    c.execute('''select dni, nome, direccion from usuarios where dni=?''', (dni,) )

    for rexistro in c.fetchall():
        print("DNI: "+ rexistro[0])
        print("Nome: " + rexistro[1])
        print("Direccion: " + rexistro[2])

except dbapi.DatabaseError as e:
    print("Erro na BD " + str(e))
import sqlite3

conn=sqlite3.connect("roster.db")


c=conn.cursor()

c.execute("""CREATE TABLE roster(
          name text,
          species text,
          age integer
          )""")

c.execute("""INSERT INTO roster VALUES ("Benjamin Sisko","Human",40),
          ("Jadzia Dax","Trill",300),
          ("Kira Nerys","Bajoran",29)""")


c.execute("""UPDATE roster 
          SET name="Ezri Dax"
          WHERE name = "Jadzia Dax"
          """)

c.execute("""SELECT * FROM roster""")

c.execute("""SELECT name, age FROM roster
          WHERE roster.species="Bajoran"
          """)


c.execute("""ALTER TABLE roster
          ADD COlUMN rank TEXT DEFAULT NULL
          """)



c.execute("""UPDATE roster 
          SET rank="Captain"
          WHERE name = "Benjamin Sisko"
          """)

c.execute("""UPDATE roster 
          SET rank="Leutenant"
          WHERE name = "Ezri Dax"
          """)
c.execute("""UPDATE roster 
          SET rank="Major"
          WHERE name = "Kira Nerys"
          """)


c.execute("""SELECT * from roster
          order by age desc""")

# c.execute("""SELECT * FROM roster""")


rosters=c.fetchall()
print(rosters)

conn.commit()

conn.close()
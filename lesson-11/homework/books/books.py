import sqlite3

conn=sqlite3.connect("books.db")

c=conn.cursor()

c.execute(""" create table books(
          title text,
          author text,
          year_published integer,
          genre text)""")

c.execute("""insert into books values("To Kill a Mockingbird","Harper Lee",1960,"Fiction"),
          ("1984","George Orwell",1949,"Dystopian"),
          ("The Great Gatsby","F.Scott Fritzgerald",1925,"Classic")""")

c.execute("""update books
          set year_published=1950
          where title="1984"
          """)



c.execute("""select title, author from books
        where genre="Dystopian"
          """)

c.execute("""delete from books
          where year_published=1950""")

c.execute("""insert into books values("1984","George Orwell",1949,"Dystopian")""")

c.execute("""alter table books
          add column rating real default null""")
c.execute("""update books
          set rating=4.8
          where title="To Kill a Mockingbird"
          """)

c.execute("""update books
          set rating=4.7
          where title="1984"
          """)
c.execute("""update books
          set rating=4.5
          where title="The Great Gatsby"
          """)



c.execute("select * from books")

c.execute("""select * from books
          order by year_published""")

print(c.fetchall())


conn.commit()

conn.close()
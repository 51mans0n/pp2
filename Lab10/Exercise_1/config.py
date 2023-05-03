import psycopg2  
con = psycopg2.connect(host = "localhost", database = "postgres", user = "postgres", password = "admin")
current = con.cursor()
current.execute('''CREATE TABLE PhoneBook(name varchar, number varchar);''')
current.close()
con.commit()
con.close()
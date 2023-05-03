
import psycopg2


def create_table():
    command = (
        '''
        CREATE TABLE snake(
            name VARCHAR (255) UNIQUE NOT NULL,
            score VARCHAR (12) NOT NULL,
            level VARCHAR (12) NOT NULL
        );
        '''
    )
    try:   
        con = psycopg2.connect(host = "localhost", database = "snake10", user = "postgres", password = "admin")
        current = con.cursor()
        current.execute(command)
        current.close()
        con.commit()

    except Exception as E:
        print(str(E))
    if con is not None:
        con.close()


create_table()
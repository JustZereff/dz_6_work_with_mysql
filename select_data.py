from connection import create_connection, database


actor_id = input(">>>")

# select_query = "SELECT * FROM actor WHERE first_name=%s"

with create_connection(database, False) as conn:
    cursor = conn.cursor()
    with open("select.sql") as sql:
        select_query = sql.read()
    cursor.execute(select_query, (actor_id, ))
    print(cursor.fetchall())
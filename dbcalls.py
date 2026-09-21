# db calls needed by the web application to successfully:
#   View the entire database table
#   Update the database table by adding a record
#   Search the database table for matching record(s)
#   Delete a record(s) from the table 

import sqlite3
from contextlib import closing

DB_NAME = "roster.db"

# Function: Connect to database
# Return: conn
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# Function: VIEW all records
# Return: results
def view_db():
    with closing(get_connection()) as conn:
        with closing(conn.cursor()) as c:
            query = "SELECT * FROM students"
            c.execute(query)
            results = c.fetchall()
    return results


# Function: ADD a record
# Input parameters: nm, addr, city
# Return msg
def add_db(nm, addr, city, id):
    with closing(get_connection()) as conn:
        with closing(conn.cursor()) as c:
            query = '''
                INSERT INTO students (name, addr, city, id)
                VALUES (?, ?, ?, ?)
            '''
            c.execute(query, (nm, addr, city, id))
            conn.commit()
    return f"{nm} added successfully"


# Function: SEARCH records
# Input parameters: nm, addr, city
# Return results
def search_db(nm, addr, city):
    with closing(get_connection()) as conn:
        with closing(conn.cursor()) as c:
            query = '''
                SELECT *
                FROM students
                WHERE (? = '' OR name LIKE ?)
                AND (? = '' OR addr LIKE ?)
                AND (? = '' OR city LIKE ?)
            '''
            c.execute(query, (nm, f"%{nm}%", addr, f"%{addr}%", city, f"%{city}%"))
            results = c.fetchall()
    return results


# Function: DELETE record
# Input parameter: nm
# Return: msg
def delete_db(nm):
    with closing(get_connection()) as conn:
        with closing(conn.cursor()) as c:
            query = '''
                DELETE FROM students
                WHERE name = ?
            '''
            c.execute(query, (nm,))
            conn.commit()
    return f"{nm} deleted successfully"

# Add the clause to execute main if this module is called directly.
# Otherwise, if imported from another module, do nothing.
if __name__ == "__main__":
    main()



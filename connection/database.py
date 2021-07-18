import sqlite3

connection = sqlite3.connect('users_data_database.db')

cursor = connection.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS users_data_table (
  id INTEGER PRIMARY KEY,
  user_email TEXT NOT NULL,
  user_password TEXT NOT NULL
);
"""

add_to_table = """
INSERT INTO
  users_data_table(user_email, user_password)
VALUES
  (?, ?);
"""

delete_from_table = """
DELETE FROM
  users_data_table
WHERE
  user_email = ?
  AND user_password = ?;
"""

read_table = """
SELECT
  user_email,
  user_password
FROM
  users_data_table;
"""


userInput = "tezequiel.gonzalez@enroutesystems.com"
passInput = "3nr0u73!"

cursor.execute(create_table)

def adding():

    data_tuple = (userInput, passInput)
    cursor.execute(add_to_table, data_tuple)
    connection.commit()

    cursor.execute("SELECT * FROM users_data_table;")
    results = cursor.fetchall()
    print(results)

#adding()

def deleting():

    data_tuple = (userInput, passInput)
    cursor.execute(delete_from_table, data_tuple)
    connection.commit()

    cursor.execute("SELECT * FROM users_data_table;")
    results = cursor.fetchall()
    print(results)

#deleting()

def selecting():

    cursor.execute(read_table)
    results = cursor.fetchall()
    for res in results:
        print(res[0])
        print(res[1])
        print("--------")

selecting()
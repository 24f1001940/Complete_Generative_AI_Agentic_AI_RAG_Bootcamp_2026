"""
Lecture 131: Tool Integration, Function Calling & SQL Database Assistants
"""

import sqlite3


def main():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE students (id INTEGER, name TEXT, score REAL)"
    )

    cursor.executemany(
        "INSERT INTO students VALUES (?, ?, ?)",
        [
            (1, "Aisha", 91.5),
            (2, "Rahul", 84.0),
            (3, "Sara", 96.0),
        ],
    )

    cursor.execute(
        "SELECT name, score FROM students WHERE score >= ?",
        (90,),
    )

    print("Students with score >= 90:")
    for row in cursor.fetchall():
        print(row)

    connection.close()


if __name__ == "__main__":
    main()

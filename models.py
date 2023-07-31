import sqlite3


class Item:
    def __init__(self):
        self.con = sqlite3.connect("items.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self) -> None:
        # self.cur.execute("""DROP TABLE items""")
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXIST items(
                number BIGINT PRIMARY KEY,
                name TEXT,
                tender_type TEXT,
                price REAL,
                days_remain INT
            )
            """
        )

    def insert(self, item: dict) -> None:
        self.cur.execute("""INSERT OR IGNORE INTO items VALUES(?, ?, ?, ?, ?)""", item)
        self.con.commit()

    def get_all(self) -> list:
        self.cur.execute("""SELECT * FROM items""")
        result = self.cur.fetchall()
        return result


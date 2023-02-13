import sqlite3


class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS data(username TEXT PRIMARY KEY, password TEXT, join_date TEXT)")
        
    def add_userdata(self, username, password, join_date):
        with self.con:
            self.con.cursor().execute("INSERT INTO data VALUES (?, ?, ?)", (username, password, join_date,))

    def check_user(self, username):
        with self.con:
            result = self.con.cursor().execute("SELECT * FROM data WHERE username = ?", (username,)).fetchall()  
            return bool(result)

    def get_user_join_date(self, username):
        with self.con:
            return self.con.cursor().execute("SELECT join_date FROM data WHERE username = ?", (username,)).fetchone()[0]

    def get_user_password(self, username):
        with self.con:
            return self.con.cursor().execute("SELECT password FROM data WHERE username = ?", (username,)).fetchone()[0]

    def delete_user(self, username):
        with self.con:
            self.con.cursor().execute("DELETE FROM data WHERE username = ?", (username,))

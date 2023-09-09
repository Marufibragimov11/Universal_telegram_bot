import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = '''
            CREATE TABLE expences IF NOT EXISTS (
                "id"	INTEGER NOT NULL,
                "sum"	INTEGER NOT NULL,
                "comment"	TEXT,
                "data"	TEXT,
                "state"	TEXT NOT NULL,
                PRIMARY KEY("id")
            );
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def add_income(self, user_id, sum, comment, data, state):
        sql = """
        INSERT INTO expences (user_id, sum, comment, date, state)
        VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(sql, (user_id, sum, comment, data, state))
        self.connection.commit()

    def get_income_data(self, user_id, month):
        self.cursor.execute(
            "SELECT sum FROM expences WHERE user_id = (?) AND date LIKE (?) AND state = 'income'",
            (user_id, f'%{month}%',))
        lst = []
        data = self.cursor.fetchall()
        for i in data:
            lst.append(i[0])
        return lst

    def get_outcome_data(self, user_id, month):
        self.cursor.execute(
            "SELECT sum FROM expences WHERE user_id = (?) AND date LIKE (?) AND state = 'outcome'",
            (user_id, f'%{month}%',))
        lst = []
        data = self.cursor.fetchall()
        for i in data:
            lst.append(i[0])
        return lst

    def get_more_indata(self, user_id, month):
        self.cursor.execute(
            "SELECT sum, comment, date FROM expences WHERE user_id = (?) AND date LIKE (?) AND state = 'income'",
            (user_id, f'%{month}%',))
        data = self.cursor.fetchall()
        return data

    def get_more_outdata(self, user_id, month):
        self.cursor.execute(
            "SELECT sum, comment, date FROM expences WHERE user_id = (?) AND date LIKE (?) AND state = 'outcome'",
            (user_id, f'%{month}%',))
        data = self.cursor.fetchall()
        return data

    def close_connection(self):
        color_reset = "\033[0m"
        color_cyan = "\033[36m"
        print(color_cyan + "Connection closed" + color_reset)
        self.connection.close()

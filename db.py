import sqlite3


class DB_Manager:
    def __init__(self, database_name: str):
        self.database = database_name


    def create_tables(self):
        con = sqlite3.connect(self.database)
        with con:
            con.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY NOT NULL,
                    pet_id INTEGER,
                    tag TEXT,
                    username TEXT NOT NULL,
                    nickname VARCHAR(35),
                    status_id TEXT NOT NULL,
                    coins INTEGER,
                    quiz_record INTEGER,
                    register_date TEXT,
                    xp INTEGER, 
                    FOREIGN KEY(pet_id) REFERENCES pets(id),
                    FOREIGN KEY(status_id) REFERENCES status_keys(id)
            )''')

            con.execute('''
                CREATE TABLE IF NOT EXISTS pets(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    parent_id INTEGER,
                    pet_name VARCHAR(35) NOT NULL,
                    max_hp INTEGER NOT NULL,
                    hp INTEGER NOT NULL,
                    max_sp INTEGER NOT NULL,
                    sp INTEGER NOT NULL,
                    def INTEGER NOT NULL,
                    str INTEGER NOT NULL,
                    xp INTEGER NOT NULL,
                    max_str INTEGER NOT NULL,
                    min_def INTEGER NOT NULL,
                    avg INTEGER NOT NULL,
                    price INTEGER,
                    xp_price INTEGER,
                    FOREIGN KEY(parent_id) REFERENCES users(id) ON DELETE CASCADE
            )''')

            con.execute('''
                CREATE TABLE IF NOT EXISTS status_keys(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    status TEXT NOT NULL
            )''')
            con.commit()


    def new_user(self,
                user_id: int,
                pet_id: int, 
                tag: str,
                username: str, 
                nickname: str, 
                status_id: int, 
                coins: int, 
                quiz_record: int, 
                register_date: str,
                xp: int):
        
        con = sqlite3.connect(self.database)
        with con:
            con.execute(f'''
                INSERT INTO users VALUES
                    ({user_id},{pet_id},'{tag}','{username}',{nickname},{status_id},{coins},{quiz_record},'{register_date}',{xp})
            ''')
            con.commit()

    def new_pet(self,
                parent_id: int,
                pet_name: str,
                max_hp: int,
                hp: int,
                max_sp: int,
                sp: int,
                defense: int,
                str: int,
                xp: int,
                max_str: int,
                min_def: int,
                avg: int,
                price: int,
                xp_price: int):
        
        con = sqlite3.connect(self.database)
        with con:
            con.execute(f'''
                INSERT INTO pets (parent_id, pet_name, max_hp, hp, max_sp, sp, def, str, xp, max_str, min_def, avg, price) VALUES
                    ({parent_id},'{pet_name}',{max_hp},{hp},{max_sp},{sp},{defense},{str},{xp},{max_str},{min_def},{avg},{price},{xp_price})
            ''')
            for row in con.execute(f'SELECT id FROM pets WHERE parent_id = {parent_id}'):
                con.execute(f'UPDATE users SET pet_id={row[0]} WHERE id={parent_id}')
            con.commit()

    def new_status(self, status_name: str):
        con = sqlite3.connect(self.database)
        with con:
            con.execute(f'''
                INSERT INTO status_keys (status) VALUES
                    ("{status_name}")
            ''')
            con.commit()


    def change(self, table: str, PK: int, column: str, value_type: int | str, value: int | str):
        con = sqlite3.connect(self.database)
        with con:
            if value_type is int:
                con.execute(f'UPDATE {table} SET {column} = {value} WHERE id = {PK}')
            elif value_type is str:
                con.execute(f'UPDATE {table} SET {column} = "{value}" WHERE id = {PK}')
            else:
                print('value_type mistake in def change')
            con.commit()
        return 'успешно изменено'


    def delete(self,table: str, PK: int):
        con = sqlite3.connect(self.database)
        with con:
            con.execute(f'DELETE FROM {table} WHERE id = {PK}')
        return 'успешно удалено'

    def read(self, table: str, PK: int, *columns: tuple):
        con = sqlite3.connect(self.database)
        with con:
            for row in con.execute(f'SELECT {','.join(columns)} FROM {table} WHERE id = {PK}'):
                return row


    def get_PK(self, table: str, col_name: str, col_content: int | str, content_type: int | str ):
        con = sqlite3.connect(self.database)
        with con:
            if content_type is int:
                for row in con.execute(f'SELECT id FROM {table} WHERE {col_name} = {col_content}'):
                    return row
            elif content_type is str:
                for row in con.execute(f'SELECT id FROM {table} WHERE {col_name} = "{col_content}"'):
                    return row
            else:
                return 'value_type mistake in def get_PK'


    def leaderboard(self, table: str,page: int, order_by: str):
        con = sqlite3.connect(self.database)
        with con:
            current_page = {}

            search_range = []
            for i in range(10):
                search_range.append(page*10-i)

            place = page*10 or len(con.execute(f'SELECT * FROM {table}'))

            iteration = 1
            if table == 'pets':
                SQL_query = f'SELECT id,pet_name,{order_by} FROM {table} ORDER BY {order_by}'
            elif table == 'users':
                SQL_query = f'SELECT nickname,{order_by} FROM {table} ORDER BY {order_by}'
            for row in con.execute(SQL_query):
                if iteration in search_range:
                    current_page[place]= row
                    place-=1
                iteration+=1
                if place == page*10-9:
                    break

        if len(current_page) < 10 and len(current_page) !=0:
            for i in range(len(current_page)):
                current_page[i+1]= current_page.pop((10-len(current_page))+i+1)
        return current_page
    
if __name__ == '__main__':
    db = DB_Manager('db.db')
    db.new_status('user')
    db.new_status('administrator')

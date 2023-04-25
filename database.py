import aiosqlite


async def create_products_table():
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT Null,
                photo_id TEXT NOT Null,
                description TEXT DEFAULT Null,
                price TEXT DEFAULT Null,
                display BOOl DEFAULT True
                )
        ''')
        await db.commit()


async def add_product(title, photo_id, price=None, description=None, display=True):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            INSERT INTO products (title, price, description, photo_id, disaplay) 
            VALUES (?,?,?,?,?)
        ''', (title, price, description, photo_id, display))
        await db.commit()


async def update_product(id, title, photo_id, price=None, description=None, display=True):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
                    UPDATE products
                    SET title = ?, price = ?, description = ?, photo_id = ?, display = ?
                    WHERE id = ?
                ''', (title, price, description, photo_id, display, id))
        await db.commit()


async def delete_product(id):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        await db.commit()


async def get_data(table_name):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        query = "SELECT * FROM {}".format(table_name)
        await cursor.execute(query)
        data = await cursor.fetchall()
        return data


async def get_value(field_name, field_value, table_name):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        query = f"SELECT * FROM {table_name} WHERE {field_name} = ?"
        await cursor.execute(query, (field_value,))
        data = await cursor.fetchall()
        await cursor.close()
        if data:
            return data
        else:
            return None

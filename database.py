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
                display BOOl DEFAULT False
                )
        ''')
        await db.commit()


async def add_product(title, photo_id, price=None, description=None, display=False):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            INSERT INTO products (title, price, description, photo_id, display) 
            VALUES (?,?,?,?,?)
        ''', (title, price, description, photo_id, display))
        await db.commit()
        return cursor.lastrowid


async def update_product(id, title, photo_id, price=None, description=None, display=False):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
                    UPDATE products
                    SET title = ?, price = ?, description = ?, photo_id = ?, display = ?
                    WHERE id = ?
                ''', (title, price, description, photo_id, display, id))
        await db.commit()


async def update_product_title(id, new_title):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET title = ?
            WHERE id = ?
        ''', (new_title, id))
        await db.commit()


async def update_product_photo_id(id, new_photo_id):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET photo_id = ?
            WHERE id = ?
        ''', (new_photo_id, id))
        await db.commit()


async def update_product_description(id, new_description):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET description = ?
            WHERE id = ?
        ''', (new_description, id))
        await db.commit()


async def update_product_price(id, new_price):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET price = ?
            WHERE id = ?
        ''', (new_price, id))
        await db.commit()


async def update_product_display(id, new_display):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET display = ?
            WHERE id = ?
        ''', (new_display, id))
        await db.commit()


async def delete_product(id):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        await cursor.execute('DELETE FROM products WHERE id = ?', (id,))
        await db.commit()


async def get_data(table_name='products'):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        query = "SELECT * FROM {}".format(table_name)
        await cursor.execute(query)
        data = await cursor.fetchall()
        return data


async def get_values(field_name, field_value, table_name='products'):
    async with aiosqlite.connect('db_train.db') as db:
        cursor = await db.cursor()
        query = f"SELECT * FROM {table_name} WHERE {field_name} = ?"
        await cursor.execute(query, (field_value,))
        rows = await cursor.fetchall()
        await cursor.close()

        if rows:
            products = []
            for row in rows:
                product = {
                    'product_id': row[0],
                    'product_title': row[1],
                    'product_photo_id': row[2],
                    'product_description': row[3],
                    'product_price': row[4],
                    'product_display': row[5]
                }
                products.append(product)

            return products
        else:
            return None

import aiosqlite

from config import DATABASE_NAME


async def create_products_table():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT Null,
                photo_id TEXT NOT Null,
                description TEXT DEFAULT Null,
                price TEXT DEFAULT Null,
                display BOOl DEFAULT False,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories (id)
                )
        ''')
        await db.commit()


async def create_categories_table():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT NOT Null
                )
        ''')
        await db.commit()


async def add_product(title, photo_id, price=None, description=None, display=False, category_id=1):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute(f'''
            INSERT INTO products (title, price, description, photo_id, display, category_id) 
            VALUES (?,?,?,?,?,?)
        ''', (title, price, description, photo_id, display, category_id))
        await db.commit()
        return cursor.lastrowid


async def add_category(category_name: str):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
            INSERT INTO categories (category_name) 
            VALUES (?)
        ''', (category_name,))
        await db.commit()
        return cursor.lastrowid


async def update_product(id, title, photo_id, price=None, description=None, display=False):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
                    UPDATE products
                    SET title = ?, price = ?, description = ?, photo_id = ?, display = ?
                    WHERE id = ?
                ''', (title, price, description, photo_id, display, id))
        await db.commit()


async def update_product_title(id, new_title):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET title = ?
            WHERE id = ?
        ''', (new_title, id))
        await db.commit()


async def update_product_photo_id(id, new_photo_id):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET photo_id = ?
            WHERE id = ?
        ''', (new_photo_id, id))
        await db.commit()


async def update_product_description(id, new_description):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET description = ?
            WHERE id = ?
        ''', (new_description, id))
        await db.commit()


async def update_product_price(id, new_price, table_name='products'):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute(f'''
            UPDATE {table_name}
            SET price = ?
            WHERE id = ?
        ''', (new_price, id))
        await db.commit()


async def update_product_display(id, new_display):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute('''
            UPDATE products
            SET display = ?
            WHERE id = ?
        ''', (new_display, id))
        await db.commit()


async def delete_product(id, table_name='products'):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        await cursor.execute(f'DELETE FROM {table_name} WHERE id = ?', (id,))
        await db.commit()


async def get_data(table_name='products'):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        query = "SELECT * FROM {}".format(table_name)
        await cursor.execute(query)
        data = await cursor.fetchall()
        return data


async def get_category(field_name, field_value):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        query = f"SELECT * FROM categories WHERE {field_name} = ?"
        await cursor.execute(query, (field_value,))
        rows = await cursor.fetchall()
        await cursor.close()

        if rows:
            categories = []
            for row in rows:
                category = {
                    'id': row[0],
                    'category_name': row[1],
                }
                categories.append(category)

            return categories
        else:
            return None


async def get_product(field_name, field_value):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        cursor = await db.cursor()
        query = f"SELECT * FROM products WHERE {field_name} = ?"
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
                    'product_display': row[5],
                    'product_category_id': row[6]
                }
                products.append(product)

            return products
        else:
            return None

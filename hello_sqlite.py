import sqlite3


db = 'first_db.sqlite'

def create_table():
    # making context managers to avoid having to commit each time
    with sqlite3.connect(db) as conn:
        # conn = sqlite3.connect('first_db.sqlite') #connect or create new
        # the database is a binary file , if it does not exist it will get created for you
        conn.execute('CREATE TABLE IF NOT EXISTS products (id int, name text)')
    conn.close()

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products values (1000,"hats")')
        conn.execute('INSERT INTO products values (1040,"jackets")')
    conn.close()

def display_all_data():
    conn = sqlite3.connect(db)
    # to save the changes
    # conn.commit()

    results = conn.execute('SELECT * from products')
    print('All products: ')
    for row in results:
        print(row) #each row is a tuple
    conn.close()

    # why didnt we have to commit on fucntions where we did nt use context managers

def display_one_product(product_name):
    conn= sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products WHERE name like ?',(product_name, ))
    first_row = results.fetchone()
    if first_row:
        print('Your product: ',first_row)
    else:
        print('not found')
    conn.close()



def create_new_product():
    new_id = int(input('Enter new id: '))
    new_name = input('Enter new product name: ')

    with sqlite3.connect(db) as conn:

        # conn.execute(f'INSERT INTO products VALUES ({new_id}, "{new_name}")') #easy to make program crash, this is not a good style
        #the better way is to use parameterized queries
        conn.execute(f'INSERT INTO products VALUES (?, ?)',(new_id, new_name))
    conn.close()

def update_product():
    updated_product = 'wool hat'
    update_id = 1000
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ?', (updated_product, update_id))
    conn.close()


def delete_product(product_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from products WHERE name = ?', (product_name, ))
    # conn.commit() #dont forget to commit
    conn.close()


create_table()
insert_example_data()
display_all_data()
display_one_product("jacket")
display_one_product("coat")
create_new_product()
update_product()
delete_product("jacket")
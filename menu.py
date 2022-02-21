"""
A menu - you need to add the database and fill in the functions. 
"""
from sqlite3 import dbapi2
from peewee import *

# Create a database instance that will manage the connection and
# execute queries
db = SqliteDatabase('menu.sqlite')


#declare a model class for each table(we have only one table). The model class then 
#  defines one or more field attributes which correspond to the table’s columns (we have #3 - ncc). 
class ChainsawRecord(Model):
    name = CharField(unique=True) #to avoid dupllicate entry, but might be a problem with 2 identical names
    country = CharField()
    catches = CharField()
    
    class Meta: 
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.catches}'

db.connect()
db.create_tables([ChainsawRecord])

#adding preliminary data
janne = ChainsawRecord(name = 'Janne Mustonen', country = 'Finland', catches = 98)
janne.save() #!important to save
ian = ChainsawRecord(name = 'Ian Stewart', country = 'Canada', catches = 94)
ian.save() #save() returns the number of rows modified.


def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    print('todo display all records')
    records = ChainsawRecord.select()
    for record in records:
        print(record)


def add_new_record():
    print('todo add new record. What if user wants to add a record that already exists?')
    new_name = input('Enter new champion name: ')
    new_country = input('Enter their country: ')
    new_catches = input('ENter their maximum number of catches: ')
    ChainsawRecord.create(name = new_name, country = new_country, catches = new_catches) #this will insert a new row into the database
    print(list(ChainsawRecord.select()))




def edit_existing_record():
    # print('todo edit existing record. What if user wants to edit record that does not exist?')
    edited_record_id = input('Enter the id for the record you want to edit: ')
    try:
        edited_record_id_found= ChainsawRecord.get_or_none(ChainsawRecord.get_by_id(edited_record_id))
        print(edited_record_id_found)
        new_catches = input('Enter the new number of catches: ')

        #update SQL statement
        new_update = ChainsawRecord.update(catches = new_catches).where(ChainsawRecord.name == edited_record_id_found.name)
        #execute to modify the database
        new_update.execute() 
    
        records = ChainsawRecord.select()
        for record in records:
            print(record)
    
    except Exception as e:
        print('That user does not exist')
        main()
    
    
        
    
    


def delete_record():
    # print('todo delete existing record. What if user wants to delete record that does not exist?') 
    name_delete = input('Enter the name of the champion you want to delete: ')
    #name_delete_found = ChainsawRecord.select().where(ChainsawRecord.name == name_delete)
    try:
        #delete sql statement
        row_delete = ChainsawRecord.delete().where(ChainsawRecord.name == name_delete)
        row_delete.execute()
        records = ChainsawRecord.select()
        for record in records:
            print(record)

    #print(row_delete)
    except Exception as e:
        print('That user does not exist')
        main()

    



if __name__ == '__main__':
    main()
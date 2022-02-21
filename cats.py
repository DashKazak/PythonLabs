from peewee import *

db = SqliteDatabase('cats.sqlite')
class Owner(Model):
    name = CharField()
    class Meta:
        datatbase = db
    def __str__(self):
        return f'{self.id}: {self.name}'

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()
    owner = ForeignKeyField(Owner, backref='cats')

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}, Owner: {self.owner}'

db.connect()
db.create_tables([Cat])

zoe = Cat(name = 'Zoe', color = 'Ginger', age = 3)
zoe.save()

holly = Cat(name = 'Holly', color = 'tabby', age = 3)
holly.save()

cats = Cat.select() #this is a query object
for cat in cats:
    print(cat)

list_of_cats = list(cats) #regular Python list

"""CRUD operations:
Create -- insert
Read --Select
Update
Delete"""

holly.age = 4
holly.save()


cats = Cat.select() #this is a query object
for cat in cats:
    print(cat)

Cat.update(age=6).where(Cat.name == 'Holly').execute()

cats = Cat.select() #this is a query object
for cat in cats:
    print(cat)

buzz = Cat(name = 'Buzz', color = 'Black', age = 3)
buzz.save()

cats_3 = Cat.select().where(Cat.age ==3)
for cat in cats_3:
    print(cat, ' is three')

        
cat_with_l = Cat.select().where(Cat.name.contains('l'))
for cat in cat_with_l:
    print(cat, ' has an l in the name')

zoe_db= Cat.get_or_none(name = 'Zoe')
print(zoe_db)

cat_1 = Cat.get_by_id(1)
print(cat_1)

total = Cat.select().count()
print(total)

total_cats_5 = Cat.select().where(Cat.age ==5).count()
print(total_cats_5)

cats_by_name = Cat.select().order_by(Cat.name)
print(list(cats_by_name))

first_3 = Cat.select().order_by(Cat.name).limit(3)
print(first_3)


row_delete = Cat.delete().where(Cat.name == 'Holly').execute()
print(row_delete, list(Cat.select()))

sam = Owner(name='Sam')
sam.save()
lily = Cat(name= 'Lily', color = 'black', age = 1, owner = sam)
lily.save()
print(lily.owner.name)


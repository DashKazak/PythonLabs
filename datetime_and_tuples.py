from datetime import datetime #for instances in time
from datetime import date #for calendar date
from datetime import time #for time in the day
#iso format next three all print 2022-01-25 format
today=date.today()
print(today)

tomorrow = date(2022,1,21)
print(tomorrow)

next_week = date.fromisoformat('2022-01-25')
print(next_week)

#instant in time--> datetime
right_now = datetime.now()
print(right_now)

#the number of seconds since Jan 1 1970
print(right_now.timestamp())

#reverse: what was the time x second from the epoch of jan 1st 1970
my_date = datetime.fromtimestamp(10000000)
print(my_date)

#useful for when working with a database that does not have a datetime property and you need to save users information in a concise standard format
#storing data in a database that does not have a built in datetime, you might convert your datetime information that represent a point in time, save it and when you process that data you can use from timestamp ti make it more readable

#tuples
city_state = [('Seattle', 'WA'),('Portland','OR'),('Minneapolis','MN')]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])

#a better way of doing it
city,state = first_city_state
print(city)

animals=('lions','puma','cat')
lion,puma,cat = animals
print(cat)

def get_distance():
    miles = 1000
    km = miles *1.6
    return miles,km
distances = get_distance()
print(distances) 
print(distances[0])
miles,km = get_distance()
print(km)



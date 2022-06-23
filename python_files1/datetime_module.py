# ***DATETIME MODULE***


import datetime

# print(dir(datetime))

# --> ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# print(help(datetime.date))

# Help on class date in module datetime.

jpsv = datetime.date(1997, 6, 1)
print(jpsv) # --> 1997-06-01
print(jpsv.year) # --> 1997
print(jpsv.month) # --> 6
print(jpsv.day) # --> 1


# *To add or substract a number of days from a date*


#Creating a new date:
mill = datetime.date(2000, 1, 1)

# Creating a time delta object and pass in the number of days:
dt = datetime.timedelta(100)

# To add 100 days:
print(mill + dt)


# By default python displays dates in  yyyy-mm--dd format, but we can specify a different format. We must create a format code, there are more than 20 different codes for you to choose from when specifying.

# If we want to display the dates like this: <Day-name, Month-name Day-#, Year> :

print(jpsv.strftime('%A, %B %d, %Y'))

# A more modern way of doing this is to create a string with this format:

message = "Juan Soto was born on {:%A, %B %d, %Y}."
print(message.format(jpsv))

# --> Juan Soto was born on Sunday, June 01, 1997.


# To create a launch 'date object' using the date class:

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
# --> 2017-03-30 
print(launch_time)
# --> 22:27:00
print(launch_datetime)
# --> 2017-03-30 22:27:00

# We can access the hour, minutes, and seconds of a 'time object':
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)

# We can access the year, month, day, hour, minute, and second of a 'datetime object':
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)


# To access the current date time the datetime class has a method called today for just this purpose:

now =datetime.datetime.today()
print(now) # --> 2022-06-12 18:19:38.981129
print(now.microsecond) # --> 981129


# Convert strings to datetimes:

moon_landing = "7/20/1969" # We have the date in a string

moon_landing_datetime =datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
# --> 1969-07-20 00:00:00

print(type(moon_landing_datetime))
# --> <class 'datetime.datetime'>
# moon_landing_datetime is an object. It is an instance of the 'datetime class' in the 'datetime module'.
#LIST
# DATA STRUCTURES: list, dictionary, tuples
# you have to know how to: create, access the elements, modify, remove elements, organized

cars = ['bmv', 'nissan', 'mazda', 'honda']
#######   0      1         2         3
# this is variables name, assign [] for list, and elements=values (index) inside.
# For Python index stars from 0

print(f"Hello Mark! Would you like to drive {cars[0].title()} or {cars[1].upper()} or {cars[2].lower()}")
# with f"string" you can write everything together and you do not have think about data types

print("I would like to own a " + str(cars[0]) + ' car')
# in this example you have convert all data in one type, and use +





#MODIFY LISTS
cars = ['bmv', 'nissan', 'mazda', 'honda']
print(cars)
print(f"before: {cars}")
cars[2] = 'tesla'
print(f"after: {cars}")




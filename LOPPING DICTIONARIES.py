##LOPPING DICTIONARIES
student1 = {'name': 'Hamza', 'gpa': 3.8, 'lastname': 'Muza'}
student2 = {'name': 'Alexa', 'gpa': 3.9, 'lastname': 'Guba'}

# looping with KEY
for key in student1.keys():
    print(key)
print()

for key in student1:
    print("key is :", key)

print()
for key in sorted(student1.keys()): # sort keys&value in alphabatic order
    print("keys is : ", key)

print()

# looping the VALUE
for value in student1:
    print("value is :", student1[value])

print()
for value in student1.values():
    print("value is ", value)

print()


# looping the values and keys at the same time
for key, value in student1.items(): # provides key and value at the same time
    print("value is ", value)
    print("key is ", key)
print()


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")
print()
print()
print()
print()
friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.upper())
    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print()
print()
print()
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")


print()
 #NESTING THE DICTINARIES
class_2020 = [student1, student2]
for student in class_2020:
    print("name of the student: ", student['name'])
    print("gpa of the student: ", student['gpa'])
print()
print()

#NESTING DICTINARIES IN DICTINARIES
dclass_2020 = {'student1': student1, 'student2': student2}
print(dclass_2020)
for key, value in dclass_2020.items():
    print("key of elements: ", key)
    print("value of elements: ", value)
    print("name of the student: ", value['name'])
    print("gpa of the student: ", value['gpa'])
    print("lastname of the student: ", value['lastname'])
print()

#### TRY IT YOUESELF
rivers = {'nile': 'egypt', 'hudson': 'usa', 'volga': 'russia', 'mississipi': 'usa', 'thames': 'uk'}
for river, country in rivers.items():
    # if country == 'usa' or country == 'uk':
    if country in ['usa', 'uk']:
        print(f"the {river.title()} runs trough {country.upper()}.")
    else:
        print(f"the {river.title()} runs trough {country.title()}.")


print()

# if i  <= n:
#     n = int(input(3))
#     print(*[num**2 for num in range(n)], sep='\n')
#
# for i in range(5):
#     print(i**2 for i in range(5))



for key, value in student1.items(): # provides key and value at the same time
    print(value)
    print(key)
print()
print()
print()
print()
print()
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
    print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
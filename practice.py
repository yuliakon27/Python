# #
# # for i in range(3): # means it will execute 3 times
# #     numbers = int(input("Enter your number: "))
# #     if numbers in range(2, 6) and numbers % 2 == 0:
# #         print("Not weird")
# #     elif numbers in range(6, 21) and numbers % 2 == 0:
# #         print("weird")
# #     elif numbers > 20 and numbers % 2 == 0:
# #         print("not weird")
# #     else:
# #         print("not weird")
# # print()
#
#
# #
# # a = int(input(3))
# # b = int(input(5))
# #
# print(a + b)
# print(a - b)
# print(a * b)
#
# massege = "Hello World!"
# print(massege)
# massege = "Hello Phyton world!"
# # print(massege)
# homework="do your homework"
#
# homework="and do not forget to read"
# print(homework)
#
# name = "Eric", "yulia"
# print(f"Hello {name[1]}, Would you like to learn some Phyton")
# lastname="Smith", "kon"
# country="USA"
# print(f"Hello {name[0]} {lastname[0]} from {country}! Are you ready to learn some Python?")
# print(name[0].upper())
# print(name[1].title())
# print(name[1].upper())
# print(name[0].lower())
# a="Albert Einstein"
# print(f'{a} once said, “A person who never made a \nmistake never tried anything new."')
# famose="The President"
# print(f'{famose} once said, "You have to try something different \nevery day!"')
# print(3*9)
# print(56/9)
# print(56-9)
# print(4**5)
# print(45//2)
# age = 34
# print("Happy " + str(age) +"'th Birthday!")
# print()
# name = ['Nirmal', 'Amrita', 'kaur', 'Olga', 'Mama', 'Sveta', 'Lena']
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# message = 'Good morning! today is your first day in the school. Your name is '
# print(message + name[0])
# print(message + name[1])
# print(message + name[2].title())
# print(message + name[3])
# print(message + name[4])
# print(message + name[5])
# print(message + name[6])
# name[6] = 'Natasha'
# print(name)
# name.append('Klepa')
# print(name)
# del name[3]
# name.remove('Klepa')
# print(name)
# name.pop(3)
# print(name)
# not_in_the_list = name.pop(0)
# print(not_in_the_list)
# print(len(name))
# print(f"{name[0].title()}, that was great trick")
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
# squares = [i**2 for i in range(1,11)]
# print(squares)
# numbers = list(range(1,1000))
# print(numbers)
# print(name[0:2])
# print(numbers[0:12])
# for num in numbers[:3]:
#     print(num)
#     print(f"this is your number")
#
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (500, 800, 900)
# print(dimensions)
# dishes = ('pizza', 'salad', 'smozi')
# for dish in dishes:
#     print(dish)
# dishes = ('spagetti', 'soup', 'smozi')
# for dish in dishes:
#     print(dish)
# age = 18
# for i in range(1000):
#     print(int(input("Please enter your number: ")))
#     if i == 42:
#         print("That is correct answer.")
#     else:
#         print("This is incorrect answer. Please try again")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")
print()
print()

partner = {
    'first_name': 'Ruslan',
    'last_name': 'Shabanov',
    'age': '31',
    'city': 'Kazan',
    'profession': 'learner'}
print(partner)
print("His name is " + partner['first_name'])
print("His lastname is " + partner['last_name'])
print("He is " + partner['age'] + " years old")
print("He was born in a small city " + partner['city'])
print("He is a life " + partner['profession'])
for key, value in partner.items():
    print("\nKey: " + key)
    print("Value: " + value)
print()
print()
fav_numbers = {
    'Lena': '45',
    'Sveta': '78',
    'Rita': '23',
    'Mama': '12',
    'Ruslan': '2'}
print("Lena's favorite number is " + fav_numbers['Lena'])
print("Sveta's favorite number is " + fav_numbers['Sveta'])
print("Rita's favorite number is " + fav_numbers['Rita'])
print("Mama's favorite number is " + fav_numbers['Mama'])
print("Ruslan's favorite number is " + fav_numbers['Ruslan'])
for key, value in fav_numbers.items():
    print("\nKey: " + key)
    print("Value: " + value)
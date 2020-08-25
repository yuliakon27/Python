# Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

# numbers = [3, 31]
# for number in range(3, 31):
#     print(number)
#
# for number in range(1, 11):
#     print(number**3)

number = [num**3 for num in range(1, 11)]
print(number)

cats = ['klepa', 'nara', 'mysay', 'rigik', 'kisa', 'kotik']
for cat in cats:
    print(f"{cat.upper()}, welcome to the family")

for cat in cats:
    print(cat.upper() + " welcome to the family," + " \n")

animals = ['cat', 'dog', 'bird']
for animal in animals:
    print(f"{animal.title()} is great pet!")
    print(f"{animal.title()} is very friendly")
print(f" All animals can be great pets")

squares = []
for value in range(1, 11):
    squares.append(value**4)
print(squares)

digits = [1 ,2, 3, 6, 9, 45, 78, 89]
print(min(digits))
print(max(digits))
print(sum(digits))


## IDE integrated development environment
# for java - eclipse, intellijIdia
# python - VScode, pycharm, VI

students = ['john', 'erik', 'yulia', '105']
print(students)
print(students[1])
print(f"Hello, {students[2].title()}! thank you for coming!")
print(f"Hello, {students[3]}! thank you for coming!")
print(f"Hello, {students[3]}! thank you for coming!")

cars = ['toyta', 'subaru', 'nisan', 'kea', 'ford']
print(f"I used to have {cars[0]}, when i was 18. it was a nice car.")
print(f"but after a few years i switched to {cars[1]}, and wasn't a good choise.")
cars[2] = 'tesla'
print(cars)
cars.append('lexis')
print(cars)
cars.insert(2, 'bike')
print(cars)

#guests = ['Lena', 'Sveta', 'Dima', 'Luba', 'Olga']

#guests[2] = 'Dasha'

#print(f"Hello {guests[0]}. Please join me for dinner on Friday at 7pm.")
#print(f"Hello {guests[1]}. Please join me for dinner on Friday at 7pm.")
#print(f"Hello {guests[2]}. Please join me for dinner on Friday at 7pm.")
#print(f"Hello {guests[3]}. Please join me for dinner on Friday at 7pm.")
#print(f"Hello {guests[4]}. Please join me for dinner on Friday at 7pm.")

def greeting(name):
    print("Hello, " + name)
greeting("Dasha")
greeting("Yulia")
greeting("Olga")
greeting("Oleg")



def my_function():
    print("Hello from my function")
my_function()

states = ['new york', 'new jersey', 'connecticut', 'virginia', 'california']



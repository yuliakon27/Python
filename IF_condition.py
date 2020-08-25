# IF condition
cars = ['audi', 'bmd', 'subaru', 'toyta']
for car in cars:
    if car == 'bmd':
        print(car.upper()) # if expression returns True, else case is skipped
    else:
        print(car.title())

if 'bmw' not in cars:
    cars.append('bmw')
print(cars)

print()
for car in cars:
    if 'bmwx5' != car.lower():
        print(f"{car} is not bmwx5")
print()
if 2 == 2:
    print('it is true')
else:
    print('it is not true')

# Multiple conditions

age = int('25')
states_17 = ['NY', 'CA', 'NC', 'VA', 'CT']
states_16 = ['NJ', 'WA', 'MA', 'TX', 'VT']

for i in range(3):
    age = int(input("Enter your age: "))
    state = input('enter your state: ').upper()

    if age >= 16 and state in states_16:
        print(f"You are eligible to apply for driving licence  in following states: \n{states_16}")
        print("Available cars in these states: ")
        for car in cars[0:2]:
            print(f"\t{car}")
    elif age >= 17 and state in states_17:
        print(f"You are eligible to apply for driving licence  in following states: \n{states_17}")
        print("Available cars in these states: ")
        for car in cars[2:3]:
            print(f"\t{car}")
    else:
        diff = 17 - age
        print(f" you will be eligible to apply for DL in {diff} years.")

print()
for i in range(3): # means it will execute 3 times
    numbers = int(input("Enter your number: "))
    if numbers % 5==0 and numbers % 3==0:
        print("BuzzFuzz")
    elif numbers % 3==0:
        print("Fuzz")
    elif numbers % 5==0:
        print("Buzz")
print()


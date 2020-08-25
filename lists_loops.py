# # WORKING WITH THE LISTS
# states = ['New York', 'New Jersey', 'Connecticut', 'California']
# # Loops - within the loop you create repeatitive actions
#
# #for variable in list_name:
# #    repetitive code here
# print(states)
# print()
# for state in states:
#     print(f"Welocome to {state}!!")
#
# # states >> 4 members >>
# # 1.1  >>1st loop/round >> state=New York    --- python does this
# # 1.2  >>     print(f"Welocome to {state}!!") -- we write this code
# # 1.3  >>     Welocome to New York!!         --- this is execution
#
# ## 2.1  >>2st loop/round >> state=New Jersey
# # 2.2  >>     print(f"Welocome to {state}!!")
# # 2.3  >>     Welocome to New Jersey!!
#
# # refactoring   >> sift +f6 or right click >> refactor >> change name
#
# # SCOPE - LIFE OF THE CODE
# for state in states:
#     print(f"Welocome to {state}!!")
#
# print("Enjoy your trip in !") # outide of the scope of varibales
#
# pizzas = ['margarita', 'hawai', 'mushroom']
# for pizza in pizzas:
#     print(f"I like {pizza}")
# print("I really like pizza!!!")


#   MAKING NUMERICAL LISTS
for num in range(5): # from 0 to 4
    print(F"My current number from  range (5): {num}")
print()

for num in range(3,6): #from 3 to 5
    print(F"My current number from range (3,6): {num}")

# list (iterable)
# mutable >> [1,3,6]
#tuple >> (1,3,6) immutable
numbers = list(range(5))
print(numbers)
print()
friends =list()
print(friends)

squares = [] # squares = []
for num in range(5, 13):
    num_sqr = num**2
    squares.append(num_sqr)
    print(num_sqr)
print(squares)






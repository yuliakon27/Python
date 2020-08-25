# def greeting(name):
#     print("Welcome, " + name)
# greeting("Yulia")
# greeting("Sveta")
# greeting("Olga")
# print()
#
# def greeting(name, department):
#     print("Welcome, " + name)
#     print("You are part of " + department)
# greeting("Yulia", "IT")
#
# print()
#
# def area_triangle(base, height):
#     return base*height/2
# area_a=area_triangle(5,7)
# area_b=area_triangle(3,8)
# sum = area_a + area_b
# print("The sum of both triangle: " + str(sum))
#
# print()
# def make_abba(a, b):
#     print(a + b + b + a)
# make_abba('Hi', 'Bye')
# print()


# def not_string(str):
#     if len(str) >= 3 and str[:3] == "not":
#         return str
#     return "not " + str
#     print(not_string)
#     # str[:3] goes from the start of the string up to but not
#     # including index 3
# not_string('candy')
# not_string('x')
# not_string('not bad')

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
missing_char('kitten', 1)

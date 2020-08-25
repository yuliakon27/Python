# dictionaries - data structure, mulable, {} {key1: value1,
# list - data structure, mutable []
# tuple - data structure, immutable ()
# stors the values as key-value pair

#students {} # empty dictionary
# students = dict() # create empty dictionary and convert to a dictionary

student1 = {'name': 'Hamza', 'gpa': 3.8}
student2 = {'name': 'Alexa', 'gpa': 3.9}
# Accessing the values of Dictionary, as in list with >> cars[0]
print(student1)
print(student1['name'], student1['gpa'])
print(f"Next student is {student2['name']} with GPA = {student2['gpa']}")

# Assigning the value
student1['gpa'] = 3.7  # if key is existing this will reset the value, new gpa=3.7
print(student1)
student1['state'] = 'NY' # if key does not exist, then it will create new key-value pair
print(student1)
print(sorted(student1)) # only sorted keys are printed as a list

del student1['state']
print(student1)

#LOPPING DICTIONARIES
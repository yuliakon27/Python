# You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

guests = ['Lena', 'Sveta', 'Dima', 'Luba', 'Olga']
print(guests)
guests.insert(0, 'mama')
guests.insert(2, 'papa')
guests.append('klepa')

print(f"final guests: {guests}")

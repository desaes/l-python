# immutable list
short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")
tuple_in_list = [("Rolf", "Bob")]
another_tuple = "Rolf", # should be avoided

friends = ("Rolf", "Bob")
friends = friends + ("Jen",)
print(friends) # ('Rolf', 'Bob', 'Jen')

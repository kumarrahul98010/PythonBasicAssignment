my_tuple = (1, 2, 3, 4, 5)
new_value = 10
modified_tuple = my_tuple[:2] + (new_value,) + my_tuple[3:]
print(modified_tuple)



squared_numbers = [x**2 for x in range(1, 11)]
filtered_numbers = [x for x in squared_numbers if x % 2 == 0]
print(filtered_numbers)


squared_dict = {x:x**2 for x in range(1,11)}
filtered_dict = {key: value for key, value in squared_dict.items() if value <5}
print(filtered_dict)

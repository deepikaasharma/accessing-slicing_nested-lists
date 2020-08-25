"""nested_list = [['a', 'b', 'c'], [1, 2, 3]]

# Use indexing to access the second element in the first nested list
element_within_nested_list = nested_list[0][1]
print(element_within_nested_list)"""


"""Slicing a nested list"""

start = 10
end = 21

num_list = list(range(start, end))
overall_list = [['a', 'b', 'c'], num_list, [6, 7, 8]]

# Assign and print the elements in indeces 2, 3, 4, 5, 6 from num_list
sublist = overall_list[1][2:7]
print(sublist)
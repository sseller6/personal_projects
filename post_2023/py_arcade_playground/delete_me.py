








source = [31, 72, 32, 10, 95, 50, 25, 18]

destination = [0, 0, 0, 0, 0, 0, 0, 0]




for item in source[2:]:
    print(item)

# index_counter = 0
# first_sub_array_begin = 0
# first_sub_array_end = 0
# first_sub_array_done = False
# second_sub_array_begin = 0
# second_sub_array_end = 0
# second_sub_array_done = False
# finished = False

# while finished != True:
#     for item in source:
#         if item < source[index_counter + 1] and item == source[-1]:
#             index_counter += 1
#             first_sub_array_done = True
#         elif item > source[index_counter + 1]:
#             first_sub_array_end = item
#             first_sub_array_done = True
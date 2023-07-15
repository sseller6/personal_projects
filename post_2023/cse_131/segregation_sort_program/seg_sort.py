# 1. Name:
#      Steven Sellers
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program's purpose is to use a segregation method to sort an array.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      Started at 2:15pm.

def main():
    """
    Lines 16 through 20 are intended for the finished product. Line 22 is a test_runner.
    """
    # list = read()
    # print(f"Unsorted list: {list} ")
    # sorted_list = sort(list)
    # print()
    # print(f"Sorted list: {sorted_list} ")
    test_runner()

    return

def test_runner():
    """
    test_runner is a function that contains all of the automatic tests.
    """
    print()
    # Test empty list
    test_empty_list = test_sort([ ])
    print(f"Test Empty List Result: {test_empty_list} ")
    print()
    # Test singular list
    test_singular_list = test_sort([99])
    print(f"Test Singular List Result: {test_singular_list}")
    print()
    # Test pivot in middle, no swapping
    test_p_middle = test_sort([49, 59, 89])
    print(f"Test Pivot in Middle, No Swapping Result: {test_p_middle}")
    print()
    # Test pivot has duplicates
    test_p_duplicate = test_sort([11, 12, 31, 89, 31])
    print(f"Test Pivot has Duplicates Result: {test_p_duplicate}")
    print()
    # Test pivot is lowest element
    test_p_lowest = test_sort([99, 11, 89])
    print(f"Test Pivot as Lowest Value Result: {test_p_lowest}")
    print()
    # Test pivot as highest element
    test_p_highest = test_sort([11, 99, 12])
    print(f"Test Pivot as Highest Value Result: {test_p_highest}")
    print()
    # Test Worst Case Scenario
    test_worst_case = test_sort([26, 93, 99, 92, 19])
    print(f"Test Worst Case Scenario Result: {test_worst_case}")
    print()
    # Test Difficult Pivot
    test_hard_pivot = test_sort([31, 31, 49, 19, 49])
    print(f"Test Difficult Pivot Result: {test_hard_pivot}")
    print()

def test_sort(array):
    sort_recursive(array, 0, (len(array) - 1))
    return array

def read():
    """
    read_file prompts the user for a file name then returns the contents as an array.
    """
    file_name = input("What is the name of the file? ")
    file = open(file_name, "r")
    array = []
    lines = file.read().split(', ')
    for line in lines:
        if not array:
            return " "
        num = int(line)
        array.append(num)
    file.close()
    return array
    
def sort(array):
    sort_recursive(array, 0, (len(array) - 1))

def sort_recursive(array, i_begin, i_end):
    """
    sort_recursive uses segregate to progress through the sorting algorithm then ends once it finishes sorting the entire array.
    """
    # This is our base case.
    if i_end - i_begin < 1 or i_end < 0:
        return array
    
    i_pivot = segregate(array, i_begin, i_end)

    sort_recursive(array, i_begin, i_pivot -1)
    sort_recursive(array, i_pivot + 1, i_end)

def segregate(array, i_begin, i_end):
    """
    segregate takes care of moving the indexes as needed.
    """
    if i_begin == i_end:
        return i_begin
    
    i_pivot = (i_begin + i_end) // 2
    #i_pivot = round(i_pivot)
    i_up = i_begin
    i_down = i_end

    # Progress i_up and i_down.
    while i_up < i_down:
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
        while i_up < i_down and array[i_down] > array[i_pivot]:
            i_down -= 1
        
        # This is where we take care of moving the pivot. THIS IS CRUCIAL.
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
            # Swap the array values of i_up and i_down.
            array[i_up], array[i_down] = array[i_down], array[i_up]

            # Check if same as the swapped value.
            if array[i_up] == array[i_down]:
                i_up += 1
    
    # Swap the array values of i_up and i_pivot.
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    return i_up

main()
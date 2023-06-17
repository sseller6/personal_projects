# 1. Name:
#      Steven Sellers
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      sort_list.py sorts a list from smallest to largest.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

def main():
    #array = read_file()
    #sorted_array = sort(array)
    #print(sorted_array)
    test_sort()
    
def test_sort():
    print()
    print(f"Test: Empty           Input: []                               Output: {sort([])}")
    print(f"Test: Singular        Input: [99]                             Output: {sort([99])}")
    print(f"Test: Small sorted    Input: [3, 6]                           Output: {sort([3, 6])}")
    print(f"Test: Small unsorted  Input: [6,3]                            Output: {sort([6, 3])}")
    print(f"Test: Sorted-even     Input: [3, 12, 26, 38, 49, 59, 64]      Output: {sort([3, 12, 26, 38, 49, 59, 64])}")
    #print(f"Test: Reversed-even   Input: [64, 59, 49, 38, 26, 12, 3]  Output: {sort([64, 59, 49, 38, 26, 12, 3])}")
    print(f"Test: Sorted-odd      Input: [3, 12, 26, 38, 49, 59, 64, 79]  Output: {sort([3, 12, 26, 38, 49, 59, 64, 79])}")
    #print(f"Test: Reversed-odd    Input: [79, 64, 59, 49, 38, 26, 12, 3]  Output: {sort([79, 64, 59, 49, 38, 26, 12, 3])}")
    print(f"Test: Duplicates      Input: [31, 55, 99, 31, 49, 49]         Output: {sort([31, 55, 99, 31, 49, 49])}")

def read_file():
    """
    read_file prompts the user for a file name then returns the contents as an array.
    """
    file_name = input("What is the name of the file? ")
    file = open(file_name, "r")
    array = []
    lines = file.read().split(', ')
    for line in lines:
        num = int(line)
        array.append(num)
    file.close()
    return array

def sort(array):
    """
    sort is the main function of the program. It takes an array as its parameter, and it sorts the array from smallest to largest.
    """
    # If array is empty, return empty array.
    if array == []:
        return []
    size = len(array)
    src = array
    num = 2
    # Lines _ through _ are for populating the destination array.
    des = []
    for item in src:
        des.append("?")
    # Lines 44 through 62 are the algorithm for finding pointers.
    while num > 1:
        num = 0
        begin1 = 0
        while begin1 < size:
            end1 = begin1 +1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 += 1
            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and src[end2 - 1] <= src[end2]:
                end2 += 1

            num += 1
            combine(src, des, begin1, begin2, end2)
            begin1 = end2
        # Swap src and des pointers.
        new_begin1 = begin2
        new_end1 = end2
        begin2 = begin1
        end2 = end1
        begin1 = new_begin1
        end1 = new_end1
    return des

def combine(source, destination, begin1, begin2, end2):
    """
    combine does one thing and one thing only; it combines the pointers into one array.
    """
    end1 = begin2
     
    for i in range(begin1, end2):
        if begin1 < end1 and begin2 == end2 or source[begin1] < source[begin2]:
            destination[i] = source[begin1]
            begin1 += 1
        else:
            destination[i] = source[begin2]
            begin2 += 1
    return destination

main()
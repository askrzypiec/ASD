import random
import time

from Algorithms import basicSearch, binSerach, Selection_sort, Insertion_sort

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
#
# my_list = [2,4,5,23,4,6,1,3,2,4,5,23,4,6,1,32,4,5,23,4,6,1,32,4,5,23,4,6,1,32,4,5,23,4,6,1,3,44]
# max=0;
# for number in my_list:
#     if number>max:
#         print("new big numba")
#         max = number
#
#
# print("max numba "+ str(max))

# III search algorithm --------------------------------------------------------------
my_list = [random.randint(1, 10) for _ in range(10000000)]
my_list.insert(9999999,44)

basicSearch(my_list,my_list.__sizeof__(),44)

# III bin search algorithm ----------------------------------------------------------
my_list.sort()
binSerach(my_list,len(my_list),44,True)
# W(len) = 0(log2(len))
# A(len) = 0(log2(len))
# S(len) = O(1)

# IV Selection-sort ----------------------------------------------------------------
list =[1,2,4,5,1,3,0]
Selection_sort(list, len(list))
# Dominating operation: comparing 2 elements
# Data size: len of sequence

# W(len) = 0(len^2)
# A(len) = 0(len^2)
# S(len) = O(1)

# IV Insertion-sort ----------------------------------------------------------------
list =[1,2,4,5,1,3,0]
Insertion_sort(list,len(list))

# Dominating operation: comparing 2 elements
# Data size: len of sequence

# Optimistic 0(len-1)
# W(len) = 0(len^2)
# A(len) = 0(len^2)
# S(len) = O(1)




#!/usr/bin/env python
# coding: utf-8

# In[1]:



import timeit
from collections import Counter
import random as rd
from sortedcontainers import SortedList
import matplotlib.pyplot as plt

# My Custom Algorithm By MouadAitOugrram2019
def ctsort(list):
    ct = Counter(list)
    listmax=max(list)
    listmin=min(list)
    slist=[]
    for i in range(listmin , listmax + 1):
        try:
            for _ in range(ct[i]):
                slist.append(i)
        except KeyError:
            pass
    return slist

def sort_with_timsort(original_list):
    original_list.sort()
    return original_list

# Create a list to store execution times for different list sizes
list_sizes = [i for i in range(7*(10**7),10**8,(10**7-7*(10**6)))]
custom_algorithm_times = []
timsort_times = []

for size in list_sizes:
    sample_data = [rd.randint(0, 10**7) for _ in range(size)]
    list1=sample_data.copy()
    list2=sample_data.copy()
    # Measure execution time of custom algorithm
    custom_start_time = timeit.default_timer()
    custom_sorted_list = ctsort(list1)
    custom_end_time = timeit.default_timer()
    custom_time = custom_end_time - custom_start_time
    custom_algorithm_times.append(custom_time)
    print(custom_sorted_list)
    # Measure execution time of Timsort
    timsort_start_time = timeit.default_timer()
    timsort_sorted_list = sort_with_timsort(list2)
    timsort_end_time = timeit.default_timer()
    timsort_time = timsort_end_time - timsort_start_time
    timsort_times.append(timsort_time)
    print(timsort_sorted_list)
    

# Plot the results
plt.plot(list_sizes, custom_algorithm_times, label='Custom Algorithm')
plt.plot(list_sizes, timsort_times, label='Timsort')
plt.xlabel('list Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Speed Test: Custom Algorithm vs. Timsort')
plt.legend()
plt.show()


# In[ ]:





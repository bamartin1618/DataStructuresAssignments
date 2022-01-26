#!/usr/bin/env python
# coding: utf-8

# In[32]:


# Import libraries

import time
import random
import copy

# Bubble Sort

def bubble_sort(array):
    
    length = len(array)
    
    for i in range(length): # Pass through the array N times, where N is the length of the array.
        
        for j in range(length-i-1): # After i passes, the final i elements will be sorted. We want to loop through the unsorted part.
            
            # For two consecutive elements, if the left element is greater than the right element, swap the elements.
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array

# Merge Sort

def merge(a, b): # Function to merge two sorted arrays.
    
    merged_array = []
    
    if not a or not b:
        return a if not b else a
    
    while (len(a) and len(b)):
        
        if a[0] < b[0]:
            merged_array.append(a[0])
            
            a.pop(0)
        else:
            merged_array.append(b[0])
            
            b.pop(0)
    
    if len(a):
        merged_array.extend(a)
    elif len(b):
        merged_array.extend(b)
    
    return merged_array

def merge_sort(array): # Recursive implementation of merge sort
    
    if len(array) <= 1: # Base case
        return array
    
    mid = len(array) // 2 # Compute the middle index of the array.
    
    # Perform a merge sort on the left and right halfs and merge the two sorted arrays. 
    
    # The merged array will be sorted.
    
    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


# Generate two arrays of random integers
array_one = [random.randint(1, 1000) for i in range(100)]
array_two = [random.randint(1, 1000) for i in range(1000)]

t0 = time.time() # For each sort, log the time after the sort is completed.
bubble_sort(copy.copy(array_one)) # Perform a bubble sort on array_one. 
# Use shallow copies of the arrays to prevent overwriting the values of the original arrays.

t1 = time.time()
merge_sort(copy.copy(array_one)) # Perform a merge sort on array_one

t2 = time.time()
bubble_sort(copy.copy(array_two)) # Perform a bubble sort on array_two

t3 = time.time()
merge_sort(copy.copy(array_two)) # Perform a merge sort one array_two
t4 = time.time()

# For each sort, compute and print the time it took to complete the sort.

print(f"Bubble Sort on 100 Elements: {t1-t0}")
print(f"Merge Sort on 100 Elements: {t2-t1}")
print(f"Bubble Sort on 1000 Elements: {t3-t2}")
print(f"Merge Sort on 1000 Elements: {t4-t3}")


# In[ ]:





# In[ ]:





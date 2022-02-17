#!/usr/bin/env python
# coding: utf-8

# # Hash Table Implementation
# 
# <p>Write a class that builds a hash table from scratch. You must implement the following features: </p>
# 
# <ul>
#     <li>Add a key-value pair to the hash table</li>
#     <li>Get a key-value pair from the hash table</li>
#     <li>Delete a key-value pair from the hash table</li>
#     <li>Hash a key using a hash function</li>
#     <li>Resize the hash-table using a load factor</li>
# </ul>
# 
# <p>The implementation is correct if each method implementation has an average time-complexity of $O(1)$</p>
# 
# <p>To test the performance of your hash table implementation, compare the time it takes to perform a task against an array.</p>

# In[1]:


import time
import pandas

class HashTable:
    
    def __init__(self, load_factor, resize_factor, buckets):
        
        self.load_factor = load_factor
        self.resize_factor = resize_factor
        self.buckets = buckets
        
        self.lookup_table = [[] for i in range(self.buckets)]
        
        self.n = 0
        
    def __setitem__(self, key, value):
        
        hashed_key = hash(key) % self.buckets
        
        found = False
        
        for index, element in enumerate(self.lookup_table[hashed_key]):
            
            if element[0] == key:
                self.lookup_table[hashed_key][index] = (key, value)
                
                found = True
                break
                    
        else:
            self.lookup_table[hashed_key].append((key, value))
        
        self.n += 1
        

        if (self.n / self.buckets) >= self.load_factor:
            self.resize(self.resize_factor)

    def __getitem__(self, key):
        
        hashed_key = hash(key) % self.buckets

        
        for element in self.lookup_table[hashed_key]:
            
            if element[0] == key:
                
                return element[1]
            
        return -1
    
    def delete(self, key):
        
        hashed_key = hash(key) % self.buckets
        
        for index, element in enumerate(self.lookup_table[hashed_key]):
            
            if element[0] == key:
                
                del self.lookup_table[hashed_key][index]

                
    def resize(self, factor):
        
        resized_size = int(factor * self.buckets)
        
        resized_lookup_table = [[] for i in range(resized_size)]
        
        for bucket in self.lookup_table:

            for key, value in bucket:
                
                hashed_key = hash(key) % resized_size
        
                resized_lookup_table[hashed_key].append([key, value])
            
        self.lookup_table = resized_lookup_table
        self.buckets = resized_size


# In[2]:


from pandas_datareader.nasdaq_trader import get_nasdaq_symbols

nasdaq_data = get_nasdaq_symbols()

table_data = nasdaq_data[['NASDAQ Symbol', 'Security Name']]

nasdaq_hash_table = HashTable(3, 2, 1000)
nasdaq_array = []

for symbol, name in table_data.to_numpy():

    nasdaq_hash_table[symbol] = name
    nasdaq_array.append([symbol, name])
    
def linear_search(array, symbol):
    
    for i, element in enumerate(array):
        if element[0] == symbol:
            return i
    return -1


# In[4]:


import random

def main():
    
    hash_table_time = 0
    array_time = 0
    
    
    for i in range(10000):
        random_symbol = random.choice(nasdaq_data['NASDAQ Symbol'].to_numpy())

        t0 = time.time()
        
        nasdaq_hash_table[random_symbol]
        
        t1 = time.time()
        
        linear_search(nasdaq_array, random_symbol)
        t2 = time.time()
        
        hash_table_time += t1-t0
        array_time += t2-t1
        
    print(f"Hash Table Approach: {round(hash_table_time, 3)} seconds")
    print(f"Array Approach: {round(array_time, 3)} seconds")
    

main()


# In[ ]:





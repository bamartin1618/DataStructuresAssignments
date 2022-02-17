#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas
import random
from pandas_datareader.nasdaq_trader import get_nasdaq_symbols

class HashTable: # Class to implement hash tables.
    
    def __init__(self, load_factor, resize_factor, buckets):
        
        self.load_factor = load_factor # The load factor is the threshold the ratio of keys to buckets must reach before the hash table is resized.
        
        self.resize_factor = resize_factor # The resize factor determines how much more space is allocated to the hash table when resizing 
        # (e.g. if the resize factor is two, after resizing, a lookup table with 50 buckets will have 100 buckets.)
        
        self.buckets = buckets
        
        self.lookup_table = [[] for i in range(self.buckets)] # Initializes the hash table.
        
        self.n = 0 # Initializes the number of keys in the hash table.
        
    def __setitem__(self, key, value): # Adds a key-value pair to the hash table.
        
        hashed_key = hash(key) % self.buckets # Computes the hash of the key.
        
        found = False
        
        for index, element in enumerate(self.lookup_table[hashed_key]):
            # Iterate through all key-value pairs in the bucket corresponding to the hash. If our key is already present, we update the key's value.
            if element[0] == key:
                self.lookup_table[hashed_key][index] = (key, value)
                
                found = True
                break
                    
        else: # The key is not present in the bucket.
            self.lookup_table[hashed_key].append((key, value))
        
        self.n += 1 # Increment the number of keys.
        

        if (self.n / self.buckets) >= self.load_factor: # Check to see if the hash table needs more space. If so, invoke the resize method on the hash table.
            self.resize(self.resize_factor)

    def __getitem__(self, key): # Gets the value corresponding to a key from the hash table.
        
        hashed_key = hash(key) % self.buckets # Computes the hash of the key.

        
        for element in self.lookup_table[hashed_key]: # Perform a search for the key in the bucket corresponding to the hash.
            
            if element[0] == key:
                
                return element[1]
            
        return -1
    
    def delete(self, key): # Delete a key from the hash table.
        
        hashed_key = hash(key) % self.buckets
        
        for index, element in enumerate(self.lookup_table[hashed_key]): # Perform a search for the key in the bucket corresponding to the hash.
            
            if element[0] == key:
                
                del self.lookup_table[hashed_key][index] # If found, delete the key.
                break

                
    def resize(self, factor): # Resizes the hash table to allocate more space.
        
        resized_size = int(factor * self.buckets)
        
        resized_lookup_table = [[] for i in range(resized_size)]
        
        # Move all key-value pairs from the present lookup table to the resized lookup table.
        for bucket in self.lookup_table:

            for key, value in bucket:
                
                hashed_key = hash(key) % resized_size
        
                resized_lookup_table[hashed_key].append([key, value])
            
        self.lookup_table = resized_lookup_table # Update the lookup table to the resized lookup table.
        self.buckets = resized_size # Update the number of buckets.


# In[2]:

nasdaq_data = get_nasdaq_symbols() # Retrieves a DataFrame of NASDAQ data.

table_data = nasdaq_data[['NASDAQ Symbol', 'Security Name']] # Extract NASDAQ symbols and their corresponding names.

nasdaq_hash_table = HashTable(3, 2, 1000) # Initialize a hash table and an empty array.
nasdaq_array = []

for symbol, name in table_data.to_numpy(): # Fill out the hash table and the array.

    nasdaq_hash_table[symbol] = name
    nasdaq_array.append([symbol, name])
    
def linear_search(array, symbol): # Searches for a symbol in an array
    
    for i, element in enumerate(array):
        if element[0] == symbol:
            return i
    return -1


# In[4]:

def main(): # Program to compare the lookup speed of a hash table compared to an array.
    
    hash_table_time = 0
    array_time = 0
    
    
    for i in range(10000):
        random_symbol = random.choice(nasdaq_data['NASDAQ Symbol'].to_numpy()) # Generate a random NASDAQ symbol.

        t0 = time.time()
        
        nasdaq_hash_table[random_symbol] # Invoke the hash table's get method on the random symbol.
        
        t1 = time.time()
        
        linear_search(nasdaq_array, random_symbol) # Invoke a linear search on the array to lookup the random symbol.
        t2 = time.time()
        
        hash_table_time += t1-t0 # Add the time it took to perform both tasks.
        array_time += t2-t1
        
    print(f"Hash Table Approach: {round(hash_table_time, 3)} seconds")
    print(f"Array Approach: {round(array_time, 3)} seconds")
    

if __name__ == '__main__':
    main()


# In[ ]:





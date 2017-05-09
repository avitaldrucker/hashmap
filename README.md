# Hashmap

This repository hosts an implementation of the hashmap data structure in Python.


## Running the tests
- Install Python.
- Clone this directory.
- Navigate to this directory in your terminal.
- Type `Python test_link.py` in your terminal and press enter.
- Type `Python test_linked_list.py` in your terminal and press enter.
- Type `Python test_hash_map.py` in your terminal and press enter.


## Implementation

With a hashmap, insertion, checks for inclusion, and deletion can all be done in constant (O(1)) time. This hashmap is implemented through a collection of linked lists. Key-value pairs are added to the hash map by hashing the key and determining the proper linked list for that key by using the modulo operator (in pseudocode, `hash(key) % num_linked_lists`). A link is appended to that linked list, and that link has as instance variables a key and value.


## Insertions and Resizing the Hashmap
Resizing is a linear operation, but when the hash map doubles in size, the number of constant ('free') insertions is equal to the previous size of the hasmap and results in amortized constant time for insertions. Because the size of the hashmap resizes as soon as the number of links is equal to the number of linked lists, there are never more links than linked lists in the hashmap.

### Checking for inclusion
Checking for inclusion require sifting through the proper linked list. In this implementation, this operation is constant because on average, there are 1 or fewer links in any given linked list, and determining the proper linked list for a given key is a constant operation. Adding a link to a linked list is a constant operation because a linked list contains as an instance variable a `tail` and uses this to append new links.

### Deletion
Deleting a link can potentially require sifting through all links in a given linked list. Because there are on average 1 or fewer links in a linked list, this is a constant operation. Deletion requires reassigning pointers between links, which is also constant.

## Hashing Functions
Using the hashed value for keys to determine the proper linked list ensures the uniformity of links across linked lists, as hashing functions are designed to maximize uniformity. This protects against pathological inputs.


## Hashmap Demo

I demonstrate the functionality of my hashmap through the demo, which uses two instances of the Hashmap class to reconcile differences between accounts after various financial transactions. Please find the input text for these transactions in `reconin.txt` and my implementations of the data parsing in the script `hash_map_demo.py` and in `account.py`

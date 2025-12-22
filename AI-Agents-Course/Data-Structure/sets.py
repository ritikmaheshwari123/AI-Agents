## Unordered, no duplicate elements

## Set Creation
my_set = {1, 2, 3}
print("Initial Set:", my_set)
print("Type of my_set:", type(my_set))
new_set = set([4, 5, 6])
print("New Set from list:", new_set)

## Empty Set
empty_set = set()
print("Type of empty_set:", type(empty_set))

set_with_duplicates = {1, 2, 2, 3, 3, 3}
print("Set with duplicates (duplicates removed):", set_with_duplicates) 

## Adding and Removing Elements
my_set.add(4)       
print("Set after adding 4:", my_set)
my_set.remove(2) # Raises KeyError if 2 not present
print("Set after removing 2:", my_set)
my_set.discard(5)  # No error if 5 not present
print("Set after discarding 5 (no error if not present):", my_set)
my_set.discard(3)
print("Set after discarding 3:", my_set)
my_set.pop()  # Removes and returns an arbitrary element
print("Set after popping an element:", my_set)
my_set.clear()  # Removes all elements
print("Set after clearing all elements:", my_set)   

## Set membership testing
another_set = {1, 2, 3}
if 2 in another_set:
    print("2 is present in another_set")
if 5 not in another_set:
    print("5 is not present in another_set")

## Mathematical Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a | set_b
print("Union of set_a and set_b:", union_set)

# Intersection
intersection_set = set_a & set_b    
print("Intersection of set_a and set_b:", intersection_set)

# Difference
difference_set = set_a - set_b
print("Difference of set_a and set_b (set_a - set_b):", difference_set)

# Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference of set_a and set_b:", symmetric_difference_set)

set_a.intersection_update(set_b)
print("set_a after Intersection_update with set_b:", set_a) 

## Sets methods
set1 = {1, 2, 3}
set2 = {3, 4, 5}

## is set1 a subset of set2?
print("Is set1 a subset of set2?", set1.issubset(set2))
## is set2 a superset of set1?
print("Is set2 a superset of set1?", set2.issuperset(set1))

lst = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(lst)
print("Unique elements from list:", unique_elements)

## counting unique words in a sentence
sentence = "This is a sample sentence with several words this is a sample"      
words = sentence.lower().split()
unique_words = set(words)
print("Unique words in the sentence:", unique_words)
print("Number of unique words:", len(unique_words))

## ordered collection of elements
## immutable (cannot be changed after creation) 


empty_tuple = ()
another_empty_tuple = tuple()
# Creating a tuple
list_tuple = tuple([1, 2, 3, 4, 5])
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print("Original Tuple:", my_tuple)

# Accessing elements
first_element = my_tuple[0]
print("First Element:", first_element)
last_element = my_tuple[-1]
print("Last Element:", last_element)

# Slicing
sliced_tuple = my_tuple[1:4]    
print("Sliced Tuple (1 to 3):", sliced_tuple)

# Tuple operations

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Repetition
repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)    

# Membership testing
is_in_tuple = 2 in tuple1
print("Is 2 in tuple1?:", is_in_tuple)

## Immutable nature
# Attempting to change an element (will raise an error) 
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)

## Tuple methods
# count() method returns the number of occurrences of a value
count_of_2 = (1, 2, 2, 3, 2).count(2)
print("Count of 2 in (1, 2, 2, 3, 2):", count_of_2)

# index() method returns the first index of the specified value
index_of_a = my_tuple.index('a')
print("Index of 'a' in my_tuple:", index_of_a)

## Packing and Unpacking
# Packing
packed_tuple = 1, 'hello', 3.14
print("Packed Tuple:", packed_tuple)

# Unpacking
a, b, c = packed_tuple
print("Unpacked Values:", a, b, c)

# Unpacking with asterisk
x, *y, z = (1, 2, 3, 4, 5)
print("x:", x)
print("y:", y)
print("z:", z)

## Nested Tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)    

# Accessing elements in nested tuples
nested_element = nested_tuple[1][0]
print("First element of second tuple in nested_tuple:", nested_element)

## Tuple Comparison
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
are_tuples_equal = tuple_a == tuple_b
print("Are tuple_a and tuple_b equal?:", are_tuples_equal)
# Lexicographical comparison
is_tuple_a_less = tuple_a < tuple_b
print("Is tuple_a less than tuple_b?:", is_tuple_a_less)

## Tuple Length
length_of_tuple = len(my_tuple)
print("Length of my_tuple:", length_of_tuple)   

## Iterating through a tuple
for element in my_tuple:
    print("Element:", element)


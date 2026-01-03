## Generators are a simpler way to create iterators using functions and the 'yield' statement to produce a series of 
## values laxily, which means values are generated on-the-fly and do not require storing the entire series in memory.

def square_numbers(n):
    for i in range(n):
        yield i * i

# Example usage:
for square in square_numbers(10):
    print(square)
# This will print the squares of numbers from 0 to 9, one at a time.

a = square_numbers(5)
print(next(a))  # Output: 0
print(next(a))  # Output: 1
print(next(a))  # Output: 4
print(next(a))  # Output: 9
print(next(a))  # Output: 16
# Using next() to get values one at a time from the generator
# If we call next() again, it will raise StopIteration as there are no more values to yield.

## Practical example: Reading large files line by line using a generator

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yielding one line at a time
# Example usage:
for line in read_large_file('large_file.txt'):    
    print(line)
# This will read and print each line from a large file without loading the entire file into memory
# at once, making it memory efficient.

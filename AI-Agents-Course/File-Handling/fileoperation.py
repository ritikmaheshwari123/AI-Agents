### Read a whole file

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

## Read file line by line

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

### Write to a file(overwrite)
with open('example.txt', 'w') as file:
    file.write('This is a new line.\n')

## write to a file(append)
with open('example.txt', 'a') as file:
    file.write('New line is appended.\n')

## Writing a list of lines to a file
lines = ['First line.\n', 'Second line.\n', 'Third line.\n']
with open('example.txt', 'a') as file:
    file.writelines(lines)

## Binary files

data = b'\x00\x01\x02\x03\x04\x05'
with open('binaryfile.bin', 'wb') as file:
    file.write(data)

with open('binaryfile.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)

### Writing then reading using seek
with open("sample.txt", "w+") as file:
    file.write("Hello, World!")
    file.seek(0)
    content = file.read()
    print(content)
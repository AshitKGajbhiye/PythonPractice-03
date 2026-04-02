#### Generators
'''Generators are a simpler way to create iterators. They use the yield keyword to produce a series of values lazily, which means they generate values on the fly and do not store them in memory.'''

def square(n):
    for i in range(3):
        yield i**2

square(3)

for i in square(3):
    print(i)

a=square(3)
# a


next(a)

def my_generator():
    yield 1
    yield 2
    yield 3

gen=my_generator()
# gen

next(gen)

for val in gen:
    print(val)

#### Practical Example: Reading Large Files
'''Generators are particularly useful for reading large files because they allow you to process one line at a time without loading the entire file into memory.'''

### Practical : Reading LArge Files

def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line

file_path='large_file.txt'

for line in read_large_file(file_path):
    print(line.strip())

#### Conclusion
'''Iterators and generators are powerful tools in Python for creating and handling sequences of data efficiently. Iterators provide a way to access elements sequentially, while generators allow you to generate items on the fly, making them particularly useful for handling large datasets and infinite sequences. Understanding these concepts will enable you to write more efficient and memory-conscious Python programs.'''


# Assignment 3

## Array.py

### Prerequisites

None, only python

### Functionality

Contains a class for creating arrays of n-dimensions.
The arrays allow adding, subtracting and multiplication,
as well as methods for comparing arrays and the elements of two arrays
It also contains a method for finding the smallest element in the array

### Missing Functionality

Allows only integers, boolians and float elements.

### Usage

You can create an array by making an instance of the class Array by for example

```python
A = Array(shape, *args)
```
Where shape is a tuple with the size of the array, and args are the arguments in the array.

With instances A and B, one can then do 

```python
A = Array(shape, *Aargs); B = Array(shape, *Bargs)

adding = A+B
subtracting = A-B
multiplying = A*B
print(A)

print(A=B)

Element_equality = A.is_equal(B)

Minimum = A.min_element()
```
The different arithmetic operations and the Element_equality function allows B to be either an number or an array.
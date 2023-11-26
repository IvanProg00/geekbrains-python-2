# Task 2

Write a function `same_by(characteristic, objects)` that checks whether all objects
have the same value of some characteristic, and returns `True` if so. If the value
of the characteristic differs for different objects, then `False`. For an empty set
of objects, the function should return True. The `characteristic` argument is a function
that takes an object and calculates its characteristic.

As an example of a characteristic, you can take the parity check from the lecture,
or you can come up with your own.

## Example

- `[1, 2, 3, 4, 5]`; `lambda: x%2 == 0` -> False

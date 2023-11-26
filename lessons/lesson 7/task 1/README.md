# Task 1

You have code that you can't change (this often happens when the code in the depths
of the program is used many times and you don't want to break anything):

```python
transformation = "<???>"
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

transormed_values = list(map(transformation, values))
```

The only way you can interact with this code is by setting the transformation function.
However, you realized that for your current task you do not need to transform the
list of values in any way, but you need to get it as it is. Write such a lambda expression
`transformation` so that `transformed_values` turns out to be a copy of `values`.

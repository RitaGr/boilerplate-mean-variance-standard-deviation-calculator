# Mean-Variance-Standard Deviation Calculator

This project is part of the freeCodeCamp Data Analysis with Python course.
It implements a function `calculate()` that takes a list of nine numbers, reshapes it into a 3x3 NumPy array, and returns a dictionary containing the mean, variance, standard deviation, max, min, and sum along each axis and for the flattened matrix.

If the input list contains fewer than nine elements, the function raises a `ValueError` with the message:

```
List must contain nine numbers.
```

## Features

* Calculates statistical measures (mean, variance, standard deviation, max, min, sum)
* Returns results for:

  * Each column (axis 0)
  * Each row (axis 1)
  * Entire flattened matrix
* Uses NumPy for efficient computation

## Example

```python
calculate([0,1,2,3,4,5,6,7,8])
```

Returns:

```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Installation and Usage

1. Clone the repository
2. Run `python3 main.py` to test the function
3. Unit tests are provided in `test_module.py`

## Acknowledgements
This project is part of the [FreeCodeCamp Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) course.

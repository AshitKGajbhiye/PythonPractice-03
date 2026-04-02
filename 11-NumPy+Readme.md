<!-- https://pynative.com/python-numpy-exercise/ -->
<!-- https://www.geeksforgeeks.org/python/numpy-tutorial/ -->
<!-- https://github.com/krishnaik06/Complete-Python-Bootcamp/blob/main/10-Data%20Analysis%20With%20Python/10.1-numpy.ipynb -->

NumPy is a core Python library for numerical computing, built for handling large arrays and matrices efficiently. It is significantly faster than Python's built-in lists because it uses optimized C language style storage where actual values are stored at contiguous locations (not object reference).

ndarray object: N-dimensional array for fast numerical operations.
Vectorized operations: Perform element-wise calculations without loops.
Broadcasting: Operate on arrays of different shapes.
Linear algebra functions: Matrix operations like multiplication and inversion.
Statistical functions: Mean, median, standard deviation.
Integration: Works with Pandas, SciPy and scikit-learn.

Why Learn NumPy?
Executes vectorized operations 10 to 100 times faster than standard Python loops.
Uses homogeneous arrays to store large datasets more compactly than Python lists.
Provides optimized functions for linear algebra, Fourier transforms and matrix manipulations.
Includes robust tools for statistics, random number generation and missing data management.
Expresses complex math in single-line commands, eliminating the need for manual, nested loops.

Below topics are covered in this exercise
Basics: imports, creation routines, identity matrices, versioning
Intermediate: Array manipulation and common operations
Indexing & Slicing: rows, columns, sub-arrays, boolean masks
Array Operations: element-wise math, dot product, normalization, stats
Random Numbers: random floats/ints, shuffling, sorting
Reshaping & Stacking: reshape, flatten, split, tile vs repeat
Boolean & Filtering: conditional filtering, replace, unique counts, set ops
Advanced: diagonals, eigenvalues/vectors, solve, inversion, structured arrays
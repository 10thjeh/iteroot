# Iteroot
### A Py package to calculate root of an equation using Newton-Raphson method

Install
-------
Download `iteroot.py` and `function.py` and put on working directory

Importing
------

```python
import iteroot
```
or
```python
from iteroot import newton
```

Usage
------
Changing the equation:
a `function.py` file is included,you can edit the `f(x)` and `df(x)` there

`f(x)` is the original function and
`df(x)` is the derived function

you can import math or numpy here if needed

Syntax:
```python
newton(int x1, int iteration, bool showIteration)
```
|Argument|Data type|Explanation|
|--------|---------|-----------|
|x1|int|Starting x_0 value|
|iteration|int|Number of iterations to do|
|showIteration|bool|Prints each iteration with print() if true, else return the latest x value|


Example
-------
Using iteroot to calculate root of ![equation](http://www.sciweavers.org/tex2img.php?eq=x%5E2%2B5x%2B6&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### function.py configuration
```python
def f(x):
    return x**2+5*x+6

def df(x):
    return 2*x+5
```
#### With showIter=true
We're using 1 as starting value of x and 20 times of iteration
```python
from iteroot import newton
newton(1,20,true)
```
Output:
```
n               x
0               -0.7142857142857142
1               -1.537142857142857
2               -1.888749470114455
3               -1.9898759348297557
4               -1.9998995374825757
5               -1.9999999899093093
6               -1.9999999999999991
7               -1.9999999999999991
8               -1.9999999999999991
9               -1.9999999999999991
10              -1.9999999999999991
11              -1.9999999999999991
12              -1.9999999999999991
13              -1.9999999999999991
14              -1.9999999999999991
15              -1.9999999999999991
16              -1.9999999999999991
17              -1.9999999999999991
18              -1.9999999999999991
19              -1.9999999999999991
```
#### With showIter=false
```python
from iteroot import newton
root = newton(1,20,false)
print(root)
```
Output:
```
-1.9999999999999991
```

To-Do
------
Calculate root based from ![equation](http://www.sciweavers.org/tex2img.php?eq=%7Cf%28x%29%7C%3C%20%5Cvarepsilon%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

Notes
-----
This package is developed in windows enviroment and python 3.8.3

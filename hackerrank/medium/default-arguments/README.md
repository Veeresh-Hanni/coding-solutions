# Default Arguments

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In this challenge, the task is to debug the existing code to successfully execute all provided test files.
________________________________________________________________________________________

Python supports a useful concept of default argument values. For each keyword argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it. For example, consider the following increment function:


```python
def increment_by(n, increment=1):
    return n + increment
```

The functions works like this:

```python
>>> increment_by(5, 2)
7
>>> increment_by(4)
5
>>>
```

Debug the given function `print_from_stream` using the default value of one of its arguments. 

The function has the following signature:

```python
def print_from_stream(n, stream)
```

This function should print the first $n$ values returned by `get_next()` method of `stream` object provided as an argument. Each of these values should be printed in a separate line.

Whenever the function is called without the `stream` argument, it should use an instance of `EvenStream` class defined in the code stubs below as the value of `stream`.

Your function will be tested on several cases by the locked template code.


**Input Format**

The input is read by the provided locked code template. In the first line, there is a single integer $q$ denoting the number of queries.
Each of the following $q$ lines contains a `stream_name` followed by integer $n$, and it corresponds to a single test for your function.

**Constraints**

- $1 \leq q \leq 100$
- $1 \leq n \leq 10$


**Output Format**

The output is produced by the provided and locked code template. For each of the queries `(stream_name, n)`, if the `stream_name` is `even` then `print_from_stream(n)` is called. Otherwise, if the `stream_name` is `odd`, then `print_from_stream(n, OddStream())` is called.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T07:12:29.085Z  

```py


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()

    for _ in range(n):
        print(stream.get_next())


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/default-arguments/problem)
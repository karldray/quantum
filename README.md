# quantum
Simulate reverse causality using quantum suicide.

```python
x = quantum.choice([1,2,3,4,5,6])  # creates 6 universes
quantum.assert_(x > 3)  # destroys universes 1,2,3
quantum.assert_(x < 6)  # destroys universe 6
print(x)  # prints either 4 or 5
```

## API

### `quantum.choice(sequence)`

Return every element of the provided sequence,
each in a different alternative universe (which this call creates).
If the provided sequence is empty, this is equivalent to `quantum.fail()`.

### `quantum.fail()`

Silently and instantaneously destroy the universe,
preventing you from observing the timeline in which this call was made.
Only useful if a previous call to `quantum.choice()` has created multiple universes.

### `quantum.assert_(condition)`

Shorthand for `if not condition: quantum.fail()`.

## Notes

*How it works:* Because you can never observe a scenario
in which `fail` has been called (since it destroys the universe),
you will necessarily observe a "fortuitous" timeline in which the values returned by `choice`
cause your program to complete without ever calling `fail`.
**Be careful to ensure that such a timeline exists!**

**Do not run a program that calls fail() unconditionally or in every timeline.**
Such a program destroys every universe in which it runs correctly, so
the only observable outcome is one in which an extremely unlikely (and potentially dangerous)
natural event prevents it from completing.

When there are multiple possible (non-`fail`ing) executions of a quantum program,
the author consistently finds himself in the lexicographically-smallest one
with respect to the iteration order of sequences passed to `choice`.
This phenomenon remains unexplained.


## Examples

#### Quantum sort

```python
def qsort(xs):
    # choose a permutation of the input
    r = quantum.choice(itertools.permutations(xs))
    # assert that it's sorted
    quantum.assert_(all(r[i - 1] <= r[i] for i in range(1, len(r))))
    # return it
    return r

print(qsort([3, 0, 5, 1, 2]))  # prints [0, 1, 2, 3, 5]
```

#### Sudoku solver

```python
def solve(board):
    '''
    Given a Sudoku puzzle as a list of 81 ints in {0,...,9}
    with 0 representing an empty cell, solve the puzzle in-place.
    '''
    for i in range(81):
        if board[i] == 0:
            neighbors = set(board[j] for group in GROUPS[i] for j in group)
            board[i] = quantum.choice(x for x in range(1, 10) if x not in neighbors)

board = [0] * 81
solve(board)
printboard(board)
```

Output:
```
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
2 1 4 3 6 5 8 9 7
3 6 5 8 9 7 2 1 4
8 9 7 2 1 4 3 6 5
5 3 1 6 4 2 9 7 8
6 4 2 9 7 8 5 3 1
9 7 8 5 3 1 6 4 2
```

See examples.py.

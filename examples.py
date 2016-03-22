from __future__ import print_function

try: xrange
except NameError: pass
else: range = xrange

import itertools
import quantum




# SORT

def qsort(xs):
    # choose a permutation of the input
    r = quantum.choice(itertools.permutations(xs))
    # assert that it's sorted
    quantum.assert_(all(r[i - 1] <= r[i] for i in range(1, len(r))))
    # return it
    return r

print(qsort([3, 0, 5, 1, 2]))  # prints [0, 1, 2, 3, 5]




# SUDOKU

# initialize board structure
def _make_groups():
    groups = [[] for _ in range(27)]
    c2g = [[] for c in range(81)]
    for c in range(81):
        row = c // 9
        col = c % 9
        box = 3 * (row // 3) + col // 3
        for i in (row, 9 + col, 18 + box):
            g = groups[i]
            g.append(c)
            c2g[c].append(g)
    return c2g

GROUPS = _make_groups()

def solve(board):
    '''
    Given a Sudoku puzzle as a list of 81 ints in {0,...,9}
    with 0 representing an empty cell, solve the puzzle in-place.
    '''
    for i in range(81):
        if board[i] == 0:
            neighbors = set(board[j] for group in GROUPS[i] for j in group)
            board[i] = quantum.choice(x for x in range(1, 10) if x not in neighbors)

def printboard(board):
    for i in range(9):
        print(*board[9*i:9*(i+1)])

board = [0] * 81
solve(board)
printboard(board)




# SCHEDULING

def roundrobin(n):
    '''
    Generate an (n-1)-day round-robin tournament schedule for n teams
    (i.e. a partition of K_n's edge set into perfect matchings).
    '''
    assert n >= 2 and n & 1 == 0
    matches_used = set()

    sched = []
    for _ in range(n - 1):
        team_used = [False] * n
        rnd = []
        # ensure each team has a match this round
        for t in range(n):
            if not team_used[t]:
                # choose an opponent for t
                u = quantum.choice(range(t + 1, n))

                # ensure u isn't already in a match this round
                quantum.assert_(not team_used[u])
                
                # ensure t and u haven't already played each other
                m = (t, u)
                quantum.assert_(m not in matches_used)

                # add this match to our data structures
                team_used[t] = team_used[u] = True
                matches_used.add(m)
                rnd.append(m)

        assert len(rnd) == n // 2 # sanity check
        sched.append(rnd)

    return sched

print(roundrobin(6))

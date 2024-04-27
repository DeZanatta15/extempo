# cython: language_level=3

def update(lattice):
    assert len(lattice) > 2 and all(len(row) == len(lattice[0]) for row in lattice), "Lattice must be at least 3x3 and rectangular."
    cdef int box_length = len(lattice) - 2
    cdef int i, j
    lattice_new = [[0 for _ in range(len(lattice))] for _ in range(len(lattice))]
    for i in range(1, box_length + 1):
        for j in range(1, box_length + 1):
            lattice_new[i][j] = update_rule(lattice, i, j)
    return lattice_new


cpdef int update_rule(lattice, int i, int j):
    cdef int n_neigh = 0
    # Get the number of rows and columns
    cdef int num_rows = len(lattice)
    cdef int num_cols = len(lattice[0])

    # Check all eight directions with boundary conditions
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue  # skip the cell itself
            ni, nj = i + di, j + dj
            # Check if the neighbor is within bounds
            if 0 <= ni < num_rows and 0 <= nj < num_cols:
                n_neigh += lattice[ni][nj]

    # Apply the rules based on the count of active neighbors
    if (lattice[i][j] == 1) and (n_neigh in [2, 3]):
        return 1
    elif lattice[i][j] == 1:
        return 0
    elif (lattice[i][j] == 0) and (n_neigh == 3):
        return 1
    else:
        return 0

def test_update_rule(lattice, int i, int j):
    return update_rule(lattice, i, j)
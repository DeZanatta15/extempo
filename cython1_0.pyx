 
# cython: infer_types=True

cimport cython

@cython.boundscheck(False)  # Disables bounds checking for the entire function
@cython.wraparound(False)  # Allows negative indexing without wrapping around
def update(int[:, :] lattice):
    cdef:
        int box_length = lattice.shape[0] - 2
        int[:, :] lattice_new = [[0 for _ in range(box_length + 2)] for _ in range(box_length + 2)]
        int i, j

    for i in range(1, box_length + 1):
        for j in range(1, box_length + 1):
            lattice_new[i][j] = update_rule(lattice, i, j)

    return lattice_new

@cython.boundscheck(False)
@cython.wraparound(False)
cdef int update_rule(int[:, :] lattice, int i, int j):
    cdef int n_neigh = (lattice[i + 1][j] + lattice[i - 1][j] +
                        lattice[i][j + 1] + lattice[i][j - 1] +
                        lattice[i + 1][j + 1] + lattice[i - 1][j - 1] +
                        lattice[i - 1][j + 1] + lattice[i + 1][j - 1])

    if lattice[i][j] == 1:
        if n_neigh in (2, 3):
            return 1
        else:
            return 0
    elif lattice[i][j] == 0 and n_neigh == 3:
        return 1
    else:
        return 0


def update(lattice):
    # Determines the size of the 'lattice' minus the outer shell.
    box_length = len(lattice) - 2
    # Creates a new lattice with the same size as the input lattice.
    lattice_new = [[0 for _ in range(box_length + 2)] for _ in range(box_length + 2)]

    # Loops over each cell inside the lattice, excluding the outer shell.
    for i in range(1, box_length + 1):
        for j in range(1, box_length + 1):
            # Updates the cell state according to the Game of Life rules.
            lattice_new[i][j] = update_rule(lattice, i, j)

    # Returns the updated lattice.
    return lattice_new

def update_rule(lattice, i, j):
    # Counts the number of alive neighbors around the cell at position (i, j).
    n_neigh = lattice[i + 1][j] + lattice[i][j + 1] + lattice[i + 1][j + 1] +               lattice[i - 1][j] + lattice[i][j - 1] + lattice[i - 1][j - 1] +               lattice[i + 1][j - 1] + lattice[i - 1][j + 1]

    # Applies the Game of Life rules to determine the next state of the cell.
    if lattice[i][j] == 1 and (n_neigh in [2, 3]):
        return 1
    elif lattice[i][j] == 1:
        return 0
    elif lattice[i][j] == 0 and n_neigh == 3:
        return 1
    else:
        return 0

def print_lattice(lattice):
    for row in lattice:
        print(' '.join(['█' if cell else ' ' for cell in row]))

# Example to initialize a small lattice with a "glider" pattern
lattice = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Run the game for 5 generations and print each generation
for _ in range(5):
    print_lattice(lattice)
    lattice = update(lattice)
    print("\nNext generation:\n")
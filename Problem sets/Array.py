array = [
          [1, 2, 3],
          [4, 5, 0],
          [7, 8, 9]
        ]

indices_pairs = [(row,col) for row in range(len(array)) for col in range(len(array[0])) if array[row][col] == 0]


for indices_pair in indices_pairs:
    row, col = indices_pair

    for i in range(len(array[0])):
        array[row][i] = 0

    for i in range(len(array)):
        array[i][col] = 0

print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in array]))

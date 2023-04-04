def pascals(rows):
    row = [1]
    print(' '.join(map(str, row)).center(rows * 2))
    for i in range(1, rows):
        current = [1]
        # removes row 2 [1  1]
        if i + (i + 1) == 2:
            continue
        for j in range(1, i):
            current.append(row[j] + row[j-1])
        current.append(1)
        print(' '.join(map(str, current)).center(rows * 2))
        row = current

# test cases
pascals(12)

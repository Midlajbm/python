
n = 4

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(1, n - i + 1):
        print(" ", end="")
    # Print descending numbers
    for j in range(i, 0, -1):
        print(j, end="")
    # Print ascending numbers
    for j in range(2, i + 1):
        print(j, end="")
    print()
    
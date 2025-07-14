n = 6  # Number of rows for each wing

# Upper part of the butterfly
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower part of the butterfly
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
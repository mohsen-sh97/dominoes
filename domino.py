def generate_matrix_and_process(n, m, matrix):
    row_results = []  # To store the row-wise results
    col_results = []  # To store the column-wise results

    # Process rows
    for row in matrix:
        a, b, c = [], [], []  # Initialize empty lists a, b, and c for each row
        counter_a, counter_b = 1, 1  # Counters for consecutive 1s and 0s

        for index, element in enumerate(row):
            if element == 1:
                a.append(counter_a)
                counter_a += 1
                counter_b = 1  # Reset counter for 0s
            else:
                b.append(counter_b)
                c.append(index + 1)  # Store the index of the 0 (1-based index)
                counter_b += 1
                counter_a = 1  # Reset counter for 1s

        row_results.append({"a": a, "b": b, "c": c})

    # Process columns
    for col_index in range(m):
        cula, culb, culc = [], [], []  # Initialize empty lists for each column
        counter_a, counter_b = 1, 1  # Counters for consecutive 1s and 0s

        for row_index in range(n):
            element = matrix[row_index][col_index]
            if element == 1:
                cula.append(counter_a)
                counter_a += 1
                counter_b = 1  # Reset counter for 0s
            else:
                culb.append(counter_b)
                culc.append(row_index + 1)  # Store the index of the 0 (1-based index)
                counter_b += 1
                counter_a = 1  # Reset counter for 1s

        col_results.append({"cula": cula, "culb": culb, "culc": culc})

    return row_results, col_results

def calculate_negative(results):
    negative = 0
    for i in range(len(results) - 1):
        current = results[i]
        next_q = results[i + 1]

        if current == next_q:  # Check if two consecutive q are identical
            negative += len(current["c"])  # Add the length of c to negative

    return negative

def count_ones(lst):
    return lst.count(1)  # Count the number of 1s in the list

def calculate_sum_of_ones(row_results, col_results):
    row_sum = sum(count_ones(result["a"]) for result in row_results)
    col_sum = sum(count_ones(result["culb"]) for result in col_results)
    return row_sum + col_sum

# Input processing
n, m = map(int, input().strip().split())
matrix = []
for _ in range(n):
    line = input().strip()
    matrix.append([1 if char == '|' else 0 for char in line])

# Process the matrix
row_results, col_results = generate_matrix_and_process(n, m, matrix)

# Calculate "negative" for rows and columns
# row_negative = calculate_negative(row_results)
# col_negative = calculate_negative(col_results)

# Calculate the sum of 1s in "a" and "culb"
sum_of_ones = calculate_sum_of_ones(row_results, col_results)

# Print the results
# print("Matrix:")
# for row in matrix:
#     print(''.join('|' if x == 1 else '-' for x in row))
#
# print("\nRow-wise Results:")
# for i, result in enumerate(row_results, 1):
#     print(f"q{i} = {result}")
#
# print("\nColumn-wise Results:")
# for i, result in enumerate(col_results, 1):
#     print(f"qcul{i} = {result}")

# print(f"\nRow Negative: {row_negative}")
# print(f"Column Negative: {col_negative}")
# print(f"Sum of 1s: {sum_of_ones}")
print(sum_of_ones)







# def calculate_negative(matrix, results):
#     negative = 0
#     for i in range(len(results) - 1):
#         current = results[i]
#         next_q = results[i + 1]
#
#         if current["a"] == next_q["a"] and current["b"] == next_q["b"]:
#             if matrix[i] != matrix[i + 1]:  # Check if corresponding rows are not identical
#                 continue  # Do not increment negative
#             if not current["b"] and not next_q["b"]:  # Both b are empty
#                 negative -= 1
#             elif not current["a"] and not next_q["a"]:  # Both a are empty
#                 continue  # Do not change negative
#             else:
#                 negative += 1
#
#     return negative
# negative = calculate_negative(matrix, results)
# print(f"\nNegative: {negative}")
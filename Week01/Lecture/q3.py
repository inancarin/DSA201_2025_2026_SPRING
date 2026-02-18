"""
matrix = [
          [1, 2, 3],
          [4, 5, 6],
          [9, 8, 9],
        ]
"""

matrix = [
          [1, 2, 3, 100, 20],
          [4, 5, 6, 30, 1000],
          [9, 8, 10, 4, 25],
          [198, 10, 20, 30, 40],
          [77, 66, 55, 44, 33]
        ]

first_total = 0
second_total = 0

for i in range(len(matrix)):
    first_total += matrix[i][i]
    second_total += matrix[i][len(matrix)-1-i]

diff = abs(first_total - second_total)
print(diff)

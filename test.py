import pandas
import cv2
import math
import os
import random
import re
import sys

def formingMagicSquare(s):
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]
    
    min_cost = float('inf')  # Start with infinity to find the minimum cost
    
    for magic in magic_squares:
        cost = 0  # Start cost from 0
        
        for i in range(3):
            for j in range(3):  # Corrected to range(3)
                cost += abs(s[i][j] - magic[i][j])  # Added abs() to calculate the cost correctly
        
        if cost < min_cost:
            min_cost = cost
    
    return min_cost

if __name__ == '__main__':
    output_path = 'output.txt'  # Define output path
    fptr = open(output_path, 'w')

    s = []

    for _ in range(3):  # Corrected to read only 3 rows
        try:
            s.append(list(map(int, input().split())))
        except EOFError:
            break  # Handle EOFError gracefully

    if len(s) == 3 and all(len(row) == 3 for row in s):  # Ensure s is a 3x3 matrix
        result = formingMagicSquare(s)
        fptr.write(str(result) + '\n')  # Converted result to str and added newline
    else:
        fptr.write("Input must be a 3x3 matrix.\n")  # Handle incorrect input size

    fptr.close()

# CodeSentinal: created for you by RuchirAdnaik.
from typing import List


def sumaM(matrix1: List[List[int]], matrix2: List[List[int]]):
    wynik = []
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix1[0])):
            temp.append(matrix1[i][j] + matrix2[i][j])
        wynik.append(temp)
    return wynik
 

a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2, 3], [4, 5, 6]]

print(sumaM(a, b))

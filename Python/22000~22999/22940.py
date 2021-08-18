from typing import List

def copyMatrix(A: List[List[int]], m: int, n: int) -> List[List[int]]:
    copy = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j])
        copy.append(row.copy())
        row.clear()
    return copy

def det(A: List[List[int]], n: int) -> int:
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        row1 = A.pop(0)
        result = 0
        for i in range(n):
            coMat = copyMatrix(A, n - 1, n)
            for j in range(n - 1):
                coMat[j].pop(i)
            result += ((-1) ** (i%2)) * row1[i] * det(coMat, n - 1)
        A.insert(0, row1)
        return result

def solveByCramer(A: List[List[int]], B: List[int], n:int):
    detA = det(A, n)
    result = []
    for i in range(n):
        copyA = copyMatrix(A, n, n)
        for j in range(n):
            copyA[j][i] = B[j]
        result.append(det(copyA, n) // detA)
    return result
    

def main():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        row = list(map(int, input().split()))
        B.append(row.pop())
        A.append(row)
    solution = solveByCramer(A, B, n)
    print(" ".join(map(str, solution)))

main()
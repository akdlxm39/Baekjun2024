import sys
input = sys.stdin.readline

MOD = 1000000007

def main():
    N = int(input())
    A = [[1, 1], [1, 0]]
    answer = matpow(A, N-1)
    print(answer[0][0])

def matpow(A, N):
    answer = [[1, 0], [0, 1]]
    tmp = A
    while N:
        if N % 2:
            answer = matmul(answer, tmp)
        tmp = matmul(tmp, tmp)
        N //= 2
    return answer

def matmul(A, B):
    B1 = list(zip(*B))
    return [[sum((a * b)%MOD for a, b in zip(lineA, lineB))%MOD for lineB in B1] for lineA in A]

main()


# def main():
#     N = int(input())
#     _, answer = func(N)
#     answer = answer * 2 * power(power(2, N), MOD-2) % MOD
#     print(answer)

# def power(X, e):
#     if e == 1:
#         return X % MOD
#     return (power(X, e//2) ** 2) * X % MOD if e%2 else power(X, e//2) ** 2 % MOD

# def func(e): #(a +- b(sqrt5))^e
#     if e == 1:
#         return 1, 1
#     a, b = func(e//2)
#     if e%2:
#         return (a**2 + 5 * (b**2) + 10 * a * b) % MOD, (a**2 + 5 * (b**2) + 2 * a * b) % MOD
#     else:
#         return (a**2 + 5 * (b**2)) % MOD, (2 * a * b) % MOD

# main()
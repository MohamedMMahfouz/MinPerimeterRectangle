def solution(N):
    # write your code in Python 3.6
    dividors = primality(N)
    min_sum = N + 1
    for i in range(len(dividors)):
        sum = dividors[i][0] + dividors[i][1]
        if sum < min_sum:
            min_sum = sum

    return min_sum * 2
    pass

def primality(n):
    i = 2
    result = [[1,n]]
    while (i * i <= n):
        if (n % i == 0):
            result.append([i, n // i])
        i += 1
    return result

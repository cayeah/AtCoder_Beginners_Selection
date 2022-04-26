N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

Alice = a[0::2]
Bob = a[1::2]

answer = sum(Alice) - sum(Bob)

print(answer)
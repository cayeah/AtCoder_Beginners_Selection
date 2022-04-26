num = int(input())
answer = list(map(int, input().split()))

flag = 0
count = 0

while True:
    for i in range(num):
        if answer[i] % 2 != 0:
            flag = 1
    if flag == 1:
        break
    for i in range(num):
        answer[i] = answer[i]//2
    count += 1

print(count)

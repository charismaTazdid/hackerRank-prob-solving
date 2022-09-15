t = int(input())
for i in range(t):
    num = input()
    f = 0
    tester = list(map(int, input().split(" ")))
    for j in range(len(tester)):
        if tester[0] >= tester[-1-f]:
            k = tester.pop(0)
            tester.append(k)
            f += 1
        else:
            k = tester.pop(-1-f)
            tester.append(k)
            f += 1
    if tester == sorted(tester, reverse=True):
        print("Yes")
    else:
        print("No")

#problem link : https://www.hackerrank.com/challenges/piling-up/problem
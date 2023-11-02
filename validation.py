# Problem: https://www.hackerrank.com/challenges/validating-the-phone-number

import re
S = int(input())

for i in range(S):
    P = input()
    v = bool(re.search('^[789]', P))
    if v == True and len(P) == 10 and P.isdigit():
        print("YES")
    else:
        print("NO")

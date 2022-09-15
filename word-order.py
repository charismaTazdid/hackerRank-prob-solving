from collections import Counter


n = int(input())

word_list = []
for i in range(n):
    word = input()

    word_list.append(word)

p = Counter(word_list)
j = 0
for k in p:
    j += 1
print(j)
print(*p.values())


# problem link: https://www.hackerrank.com/challenges/word-order/problem

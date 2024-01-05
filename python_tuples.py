
# Problem: https://www.hackerrank.com/challenges/python-tuples

def func(n, m):
    t = tuple(m)
    return hash(t)
    
n = int(input())
m = map(int, input().split())

result = func(n, m)
print(result)
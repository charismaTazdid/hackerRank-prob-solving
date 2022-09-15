# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
    K, M = list(map(int, input().split()))
    
    lst = [list(map(int, input().split()))[1:] for _ in range(K)]
       
    lst2 = [list(map(lambda x: x**2, i)) for i in lst]
    
    print(max([sum(j) % M for j in product(*lst2)]))


#problem Link: https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
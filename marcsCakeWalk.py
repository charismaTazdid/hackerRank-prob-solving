# Problem: https://www.hackerrank.com/challenges/marcs-cakewalk 


def marcsCakewalk(calorie):
    result = 0
    calorie.sort(reverse=True)
    for index,value in enumerate(calorie):
        result+=(pow(2,index)*value)
    return result
        
# Problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

import re

def fun(s):
    pattern = r'^[^@]*@[^@.]*\.[^@.]*$'     # To ensure that @ and . comes exactly one time
    if not bool(re.match(pattern, s)):
        return False
    user, web, comp = s.split('@')[0], *s.split('@')[1].split('.')
    user_pattern = r'^[a-zA-Z0-9-_]+$'
    web_pattern = r'^[a-zA-Z0-9]+$'
    comp_pattern = r'^[a-zA-Z]{1,3}$'
    
    return all([re.match(user_pattern, user) is not None, re.match(web_pattern, web) is not None, re.match(comp_pattern, comp) is not None])
    
    
    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
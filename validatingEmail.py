# Problem: https://www.hackerrank.com/challenges/validating-named-email-addresses

import email.utils
import re

n=int(input())
name_email_list=[input() for _ in range(n)]


for name_mail in name_email_list:

    name, email_name =email.utils.parseaddr(name_mail)
    reg_exp=r'^[a-zA-Z]{1}[0-9a-zA-Z\-\._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    m=re.match(reg_exp,email_name)
    try:
        m.group()
        print(email.utils.formataddr((name, email_name)))
    except AttributeError:
        continue


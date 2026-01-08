import re
import email.utils

n = int(input())

pattern = r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(n):
    name, addr = email.utils.parseaddr(input())
    if re.match(pattern, addr):
        print(email.utils.formataddr((name, addr)))

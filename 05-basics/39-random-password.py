from random import choice
import string as s

length = 10
chars = s.ascii_letters + s.digits
pwd = [choice(chars) for i in range(length)]
pwd = "".join(pwd)

print(pwd)

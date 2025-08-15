from datetime import datetime as dt

now: dt = dt.now()

fmt1: str = f"{now:%d-%m-%y}"
fmt2: str = f"{now:%d-%m-%Y}"
fmt3: str = f"{now:%a %d %b %y}"
fmt4: str = f"{now:%A, %d %B %Y}"
fmt5: str = f"{now:%I:%M:%S %p}"

print(fmt1)
print(fmt2)
print(fmt3)
print(fmt4)
print(fmt5)
print(f"{now:%c}")

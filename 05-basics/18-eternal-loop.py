import time
from itertools import cycle

speakers = [("Tushan", 1), ("Kaniz", 3), ("Shahriar", 0.8), ("Dolon", 2), ("Amrin", 1)]
speaking = cycle(speakers)

while True:
    speaker, duration = next(speaking)
    print(f"{speaker = }\t is speaking for {float(duration)} second(s)")
    time.sleep(duration)

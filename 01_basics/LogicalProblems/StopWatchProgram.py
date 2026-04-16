import time

input("Press Enter to START stopwatch...")
start = time.time()

input("Press Enter to STOP stopwatch...")
end = time.time()

elapsed = end - start

print("Elapsed Time:", elapsed, "seconds")
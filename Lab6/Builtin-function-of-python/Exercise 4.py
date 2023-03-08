import time
import math

value = int(input())
expectation = int(input())

time.sleep(expectation / 1000)
print(f"Square root of {value} after {expectation} miliseconds is {math.sqrt(value)}")
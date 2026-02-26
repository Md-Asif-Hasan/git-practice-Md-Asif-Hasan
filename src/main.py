import utils
from datetime import datetime

name = input("Enter your name: ")

print(f"Your name is: {name}")
print(f"Current time is: {datetime.now()}")

print(utils.add(5, 5)) 
print(utils.sub(10, 5))

# import math

# math.sqrt(16)

from math import sqrt,pi
import random
import datetime
import os
import pandas as pd

print(sqrt(25))
print(pi)


print(random.randint(0,10))

choice = random.choice(['apple','banana','cherry'])
print(choice)

now = datetime.datetime.now()
print(now)

today = datetime.date.today()
print(today)

print(os.getcwd())
df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
print(df)
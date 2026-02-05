# STANDAR LIBRARY
import datetime

data_time = datetime.datetime.now()
print(data_time)
print(f"Year > {data_time.year}") #in Library datetime
print(f"Day > {data_time.strftime('%A')}") #in Library datetime

# Collection
from collections import Counter

count = 0
data = ["a", "b", "c", "d", "a", "c", "d", "a"]
for i in data:
    if i == "a":
        count += 1
print(count)

# - Simply
data = [
    "Termulator", 
    "bahLEL",
    "praboGO", "GibRUN",  "Termulator","praboGO", "jokoUI", "Termulator"
]
data_count = Counter(data)

print(f"Data Count = {data_count}")
print(f"Jumlah Termulator = {data_count['Termulator']}")
print(f"Jumlah Termulator = {data_count['praboGO']}")

# - Read TEXT
import io

file = io.open("Read_TEXT.txt", "r")
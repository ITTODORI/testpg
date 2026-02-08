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
    "praboGO",
    "GibRUN",
    "Termulator",
    "praboGO",
    "jokoUI",
    "Termulator"
]
data_count = Counter(data)

print(f"Data Count = {data_count}")
print(f"Jumlah Termulator = {data_count['Termulator']}")
print(f"Jumlah praboGO    = {data_count['praboGO']}")

# - Read TEXT
# import io

# file = io.open("Read_TEXT.txt","r")
# print(file.read())

# GUI : Graphical User Interface
import tkinter as tk

app = tk.Tk()
app.configure(bg="black")
app.geometry("1080x1920")
app.resizable(False,False)
app.title("Mini Apps")

# Frame Input
input_frame = 

app.mainloop()
# FILE INPUT & OUTPUT
# 1\ file I/O (Input/Output)

# Mode File
# r # to Read
# w # to Write
# a # to Append
# x # to Creat
# write(string)
print("=== TITLE DATABASE ===")
file = open("12-DATABASE.txt", "w")

while True:
    hero = input("Hero: ")
    if hero == "":
        break
    stats = input("Stats: ")

    file.write(hero + "," + stats + "\n")
    print("Database", hero, "has saved")

file.close()
print("=== Program is DONE! ===")

# 2\ Read file
print("===| OPEN FILE |===")
file = open("12-DATABASE.txt", "r")

for line in file:
    data = line.strip().split(",") # mengubah ","
    print(data[0], ":", data[1])
file.close()
print("====================")

# 3\ With Statement (Recomended)
print("===| Open DATABASE |===")
with open("12-DATABASE.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        print(data[0], "> ", data[1])
print("====================") # so simple code, not file.close

# 4\ Error Handling file
print("===| Open DATABASE |===")

try:
    with open("DATABASE.txt", "r") as file: # EROR FileNotFound
        for line in file:
            data = line.strip().split(",")
            print(data[0], "> ", data[1])
except FileNotFoundError:
    print("DATABASE PALSU!")

print("====================")

# 5\ IMPORT
import fileIMPORT

print(fileIMPORT.hero) #print import by variable 'hero'

result = fileIMPORT.data(8,2) #configuration file import in variable 'data'
print("Rate > ",result)
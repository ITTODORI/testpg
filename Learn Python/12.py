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

    file.write(hero + ", " + stats + "\n")
    print("Database", hero, "has saved")

file.close()
print("=== Program is DONE! ===")
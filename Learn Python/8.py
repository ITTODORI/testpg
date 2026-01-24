# DATA STRUCTURE
# 1\ List : variabel ini sangat dinamis bisa campuran, hanya huruf/angka.
listEmpty  = []
print(listEmpty)

topHero = ["Termulator","Bahlol", "PraboGO", "luHUB"]
print(topHero)

statHero = ["Termulator", 90, "Bahlol", 60, "PraboGO", 85]
print(statHero)

# 2\ Manipulation
skill = [
    "Termul : Kekuatan Dinasi Wo (Pasif)", 
    "Termul : Ijazah Palsu (Basic)", 
    "GibRUN : Rain Arrow 19jt LOKER (AoE)", 
    "Nyawit : racun MBG sawit (Ultimate)"
    ]
print(skill[0])
print(skill[1])
print(skill[2])
print(skill[3])

pangkat = ["Honorer", "Karyawan MBG", "PNS"]
print (pangkat)
pangkat[1] = "PPPK" #switch item
print(pangkat)

kasta = ["Dinasti Wo", "Pejabat"]
print(kasta)
kasta.append("Boomer")  #add item
print(kasta)
kasta.insert(1, "dole bludger") #custom add item
print(kasta)
kasta.remove("Dinasti Wo") #remove item
print(kasta)
kasta.pop() #remove endItem
print(kasta)

del kasta[0] #delete ex add/custom item
print(kasta)

jasa = ["Honorer", "Freelancer", "Ustadz"]
print(len(jasa))

# Combination
hotel = [1,2,3,4,5]
print(hotel)
room = [6,7,8,9,10]
print(room)

combined = hotel + room
print(combined)

dailyQuest = [
    "- Pray",
    "- Hardwork",
    "- GYM",
    "- Boxing",
    "- Rest"
    ]
for daily in dailyQuest:
    print(daily)
#and can u code
for i in range(0, len(dailyQuest)):
    print(dailyQuest[i])
#Check Items
if "- Pray" in dailyQuest:
    print("it's Item")
else:
    print("not found")

# 3\ Tuple
# tidak bisa operasi untuk Edit/Hapus data (Permanen)
point = (5,10)
print(point[0])
print(point[1])

date = (2,9,1998)
print("Date: ", date)

for e in date:
    print(e)
    
for i in range(len(date)):
    print(date[i])

# 4\ Dictionary {key-value}
#Dictionary Data
spyDocument = {
    "Name" : "Mulyono",
    "Officiate" : 2014,
    "Periode" : "2 Periode",
}
print(spyDocument)
print(spyDocument["Name"])
print(spyDocument["Periode"])

#Edit Value
spyDocument["Officiate"] = 2018
print(spyDocument)
#Delete key-value
del spyDocument["Periode"]
print(spyDocument)
#Int/switch key
for key in spyDocument:
    print(key,":", spyDocument[key])
#Int/switch key-value pairs
for key, value in spyDocument.items():
    print(key,"=", value)

# 4\ Set
title = {
    "DPR",
    "PNS",
    "MBG"
}
title.add("PPPK")
print(title)
title.remove("MBG")
print(title)
for i in title:
    print(i)
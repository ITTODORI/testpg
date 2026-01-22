# DATA STRUCTURE
# 1\ List : variabel ini sangat dinamis bisa campuran, hanya huruf/angka.
listEmpty  = []
print(listEmpty)

topHero = ["Termulator","Bahlol", "PraboGO", "luHUB"]
print(topHero)

statHero = ["Termulator", 90, "Bahlol", 60, "PraboGO", 85]
print(statHero)

# 2\ Manipulation
skill = ["Termul : Kekuatan Dinasi Wo (Pasif)", "Termul : Ijazah Palsu (Basic)", "GibRUN : Rain Arrow 19jt LOKER (AoE)", "Nyawit : racun MBG sawit (Ultimate)"]
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
kasta.pop()
print(kasta)

del kasta[0] #delete ex add/custom item
print(kasta)

jasa = ["Honorer", "Freelancer", "Ustadz"]
print(len(jasa))

# Combination
SAR = [1,2,3,4,5]
print(SAR)
Relawan = [6,7,8,9,10]
print(Relawan)

combined = SAR + Relawan
print(combined)
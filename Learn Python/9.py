# FUNCTION
# 1\ Example Function
def govt_function():
    print("Apa ada fungsinya pemerintah?!") #run
    
#run function    
govt_function()
govt_function()

# 2\ Parameter
def pejabat(nama):
    print("WOI babu", nama)
    print("Lu kerjanya ngapain aja sih?!")

pejabat("Bahlol")
pejabat("luHUB")

def info(lahan, sawit):
    pekerja = lahan * sawit
    print("Tenaga Kerja: ", pekerja, "Pekerja")

info(250, 76000)

# 3\ Return value
def lahanSawit (radius):
    karyawan=76000
    luas= karyawan * radius * radius
    return luas
luas1 = lahanSawit(20)
luas2 = lahanSawit(10)

print("luas lahan sawit bahLOL:", luas1)
print("luas lahan sawit luHUB:", luas2)

# 4\ Default Parameter
def name(cmd, bot="Nyawit nih"):
    print(bot, cmd)

name("Mulyono")
name("luHUB")

# 5\ Keyword Argument
def doksil(name, term, title):
    print("Name:", name)
    print("Term:", term, "Periode")
    print("Title:", title)
    print("-----------------")

doksil("Mulyono", 2,"President") #Positional
doksil(name="Mulyono", title="President", term=2)
doksil("luHUB", term=5, title="Dewan Ekonomi")
doksil(name="bahLOL", term=5, title="Mentri")

def doksil(name, term, title="Pejabat", jobdesk="DI PECAT!"):
    print(f"===DOKSIL {name.upper()}===")
    print(f"Term = {term} Periode")
    print(f"Title = {title}")
    print(f"Jobdesk = {jobdesk}")
    print("-----------------")

doksil("Mulyono", 2, "President")
doksil("luHUB", 1, jobdesk="Nyusahin Rakyat")
doksil("bahLOL", 1, jobdesk="Rusakin Rakyat")

# 6\ Local Variable
def lahan_sawit():
    # Local Variable
    total_lahan = 500 
    print(f"Total lahan Nyawit: {total_lahan} hektar")

lahan_sawit()
# print(total_lahan) # Ini akan ERROR! cause localVariable

# 7\ Global Variable
status = "Halal"

def check_status():
    global status
    status = "Haram" # Ini akan mengubah variable di luar juga
check_status()
print(status)

realName = "JokoUI"

def data():
    global realName
    realName = "Mulyono"

data()
print(realName)

# 7\ Parameter Dinamic
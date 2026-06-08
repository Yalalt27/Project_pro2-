'''
with open ("min_fil.txt","w") as fil:
      fil.write("Detta är en exempeltext som skrives till filen.")
      fil.write("Du kan skriva flera rader med text.")

print("Texten är skriven till filen min_fil.txt")
import os 
print(os.getcwd())

# 1. 3 мөр текст бичих
with open("d:\\exempel.txt", "w") as fil:
    fil.write("Första raden\n")
    fil.write("Andra raden\n")
    fil.write("Tredje raden\n")

# 2. Файлыг унших
with open("d:\\exempel.txt", "r") as fil:
    print("Innehåll efter första skrivningen:")
    print(fil.read())

# 3. Нэг мөр нэмэх
with open("d:\\exempel.txt", "a") as fil:
    fil.write("Fjärde raden\n")

# 4. Дахин унших
with open("d:\\exempel.txt", "r") as fil:
    print("Innehåll efter tillägget:")
    print(fil.read())
    '''
with open ("kompisar.txt","w") as file:
      file.write("Anna\n")
      file.write("Bat\n")
      file.write("Erik\n")
with open ("kompisar.txt","r") as file:

      for line in file:
            line = line.strip()
            print(f"Hej, {line}, Trevlig helg")

import os
deltagarna = ['Samer', 'Olivia', 'Ove', 'Sara']

# Skapa mappen 'my_friends' om den inte redan finns
if not os.path.exists('d:\my_friends'):

    os.makedirs('d:\my_friends')

# Skriv till filen 'exempel.txt' inuti mappen 'my_friends'
with open('d:\my_friends\exempel.txt', 'w') as fil:

    for y in deltagarna:

      fil.write('Hej ' + y + '!\n')


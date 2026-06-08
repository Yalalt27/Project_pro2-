'''
counter = {
"!":0,
"@": 0,
"#": 0,
}
with open("character.txt", "r") as file:
 content = file.read()
for char in content: 
    try:


      counter[char] = counter[char]+ 1 #counter[char] += 1
    except:
     print("The character is not !, @ or #")

print(counter)

#1 
def main():
  elever = {}
  while True:
    print("Menu:")
    print("1. Lägg till en elev")
    print("2. Ta bort en elev")
    print("3. Visa alla  elever")
    print("4. Avsluta")

    val = input("Ange ditt val:")
    if val == "1":
      Namn = input("Ange elevens namn:")
      ålder = int(input("Ånge elevens ålder:"))
      elever[namn] = ålder
      print(f"Eleven{namn} har lagts till.")
      
    elif val == "2":
      namn = input("Ånge namn på eleven du vill ta bort:")
      if namn in elever:
        del elever[namn]

      print(f"Eleven{namn} har tagits bort.")
    else:
        print("Kunde inte hitta eleven {namn}.")

    elif val == "3":
    
    if elever:
        for namn,ålder in elever.items():
          print(f"{namn} - {ålder} år") 
        else:
          print("Det finnss inga elever i klassen")

        break
    else:
        print("Felaktigt val. Försök igen.")
main()
'''

#2
library = {}
def add_book():
      title = input("Ånge bokens titel:")
      author = input(" Ånge författerens namn:")
      library[title] = author
      print(f"{title} av {author} har lagts till i bibiloteket.")

def modify_book():
      title = input("Ånge titelen på boken att modifiera:")
      if title in library:
            new_auther = input("Ånge nyas författerens namn;")
            library[title]=new_auther
            print(f"Information for {title} har updaterats. Ny författerens namn {new_auther}.")
      else:
            print(f"Boken med titelen {title} finns inte i bibolioteket. ")

def remove_book():
      title = input("Ånge titelen på boken att ta bort")
      if title in library:
            del library[title]
            print(f"{title} har tagits bort från biblioteket")
      else:
            print(f"Boken med titelen {title} finns inte biblioteket")

def print_library():
      print("Bibliotekets böcker")
      for title, author in library.items():
            print(f"{title} av {author}")

while True:
      print("Välj en åtgärd:")
      print("1. Lägg till en bok i biblioteket")
      print("2. Modifiera en boks information i biblioteket")
      print("3. Ta bort en bok från biblioteket")
      print("4. Visa en lista över alla böcker i biblioteket")
      print("5. Avsluta")

      choice = input("Ånge ditt val:")
      if choice == "1":
            add_book()
      elif choice == "2":
            modify_book()
      elif choice == "3":
            remove_book()
      elif choice == "4":
            print_library()
      elif choice == "5":
            print("Programmet avslutas")
            break
      else:
            print("Ogilitig val. Var god försök igen.")
            

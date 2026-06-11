'''
def Hälsa(name):
      medellande = "hej, "  +  name   + " Välkommen"
      return medellande 
result = Hälsa("Yalalt")
print(result)

def list (lista):
      My_list = []
      for element in lista:
            the = pow (element, 2)
            My_list.append(the)
      return My_list
print(list([2,3,4,5,6,7,8,9]))


def bokstav (mening):
      v = ""
      for i in mening:
            if i == "Ö":
                  v = v + "O"
            elif i == "ö":
                  v = v + "o"
            else:
                  v = v + i
      return v
print(bokstav("Ön nära östermalm"))


def add (a,b):
      return a + b

def sub (a,b):
      return a - b

def mul (a,b):
      return a * b

def div (a,b):
      if b == 0:
            print ("Fel: inte division 0")
      return a / b
num1 = float(input("Skriva första nummer"))
num2 = float(input("Skriva andra nummer"))

print("Det är add",add(num1,num2))
print("Det är sub",sub(num1,num2))
print("Det är mul",mul(num1,num2))
print("Det är div",div(num1,num2))

def rekna(lön):
      return sum(lön) / len(lön)
löner = int(input("Hur många löner vill du mata in:"))
lön = []
for i in range(löner):
      medel_lön = float(input(f"ånge löner {i+1}"))
      lön.append(medel_lön)
print("Ditt medel lön är",rekna(lön))
'''
def check_guess(secret_number,guess):
      if guess == secret_number:
            return True
      return False
secret_number = 7
while True:
      guess = int(input("gissa nummer"))
      if check_guess(secret_number,guess):
            print("rätt")
            break
      else:
            print("Fel: Försöko igen")
            








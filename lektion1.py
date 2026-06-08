'''

def hälsa (namn):
      medellande = "Hej " + namn + "! välkommentill våran sida"
      return medellande
resultat = hälsa ("Yalalt")
print(resultat)

def list(list):
      nylista=[]
      for element in list:
            nyttelement = pow (element,2)
            nylista.append(nyttelement)
      return nylista
print(list([2,4,5,6,7,10]))



def bokstavByte(mening):
      v = ""
      for bokstav in mening:
            if bokstav == "Ö":
                  v = v + "Ö"
            elif bokstav =="ö":
                  v = v + "ö"
            else:
                  v = v + bokstav
      return v 
print(bokstavByte("Ön nära östermalm"))



def add (a, b):
      return  a + b 
def sub (a, b):
      return a - b 
def mult (a, b):
      return a * b
def div (a,b):
      return a / b

x = float(input("enter first number"))
y = float(input("enter second number"))

print("Addition", add (x,y))
print("subtraction", sub (x,y))
print("multioliktion", mult (x,y))
print("division", div (x,y))



def meddellon(loner):
      return sum(loner) / len(loner)
antal = int(input("hur manga loner vill du mata in:"))

loner = []
for i in range (antal):
      lon = float(input("Ange lön:"))
      loner.append(lon)
print("Medellön:", meddellon(loner))
'''


def kontrollera_gisning(gissning, hemlighet_nummer ):
      return gissning == hemlighet_nummer

hemlighet_nummer = 7 

while True:
      gissning = int(input("Gissa ett nummer:"))

      if kontrollera_gisning(gissning, hemlighet_nummer):
            print("Rätt gissat")
            break
      elif gissning < hemlighet_nummer:
            print("För lågt försok igen.")
      else:
            print("För högt föraok igen")







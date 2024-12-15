import random
fanclehp=ractanglehp=1000
f=[1,2,3]
print("----------FANCLE VS RACTNGLE----------")
name=input("\nYOUR NAME HERE:")
while True:
    ac=input(f"\nYOUR HP:{ractanglehp}\nFANCLE'S HP:{fanclehp}\n1:USE THE HAMMER\n2:POWERFULL PUNCH\n3:HEAL\nANYTHING ELSE:SKIP\nMOVE:")
    #game loop
    acf=random.choice(f)
    if ac=="1":
        fanclehp-=50;print("\nTOOK 50 HP")
        acf=random.choice(f)
    if ac=="2":
        fanclehp-=75;print("\nTOOK 75 HP")
        acf=random.choice(f)
    if ac=="3":
        ractanglehp+=10;print("\nHEAL 10 HP")
        acf=random.choice(f)
    if acf==1:ractanglehp-=50;print("\nTOOK 50 HP")
    if acf==2:ractanglehp-=100;print("\nTOOK 100 HP")
    if acf==3:fanclehp+=20;print("\nHEAL 20 HP")
    if fanclehp<=0:print(f"\n{name} WINS");break
    elif ractanglehp<=0:print("\nFANCLE WINS");break

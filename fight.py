import random
fanclehp=ractanglehp=1000
bro=0
print("----------FANCLE VS RACTNGLE----------")
name=input("\nYOUR NAME HERE:")
while True:
    ac=input(f"""
YOUR HP:{ractanglehp}
FANCLE'S HP:{fanclehp}
    1:USE THE HAMMER
    2:POWERFULL PUNCH
    3:HEAL
    MOVE:""")
    #game loop
    if ac not in["1","2","3"]:bro=1
    else:bro=0
    if bro:...
    else:
        acf=random.randint(1,3)
        if ac=="1":
            fanclehp-=50;print("\nTOOK 50 HP")
        elif ac=="2":
            fanclehp-=150;print("\nTOOK 150 HP")
        elif ac=="3":
            ractanglehp+=10;print("\nHEAL 10 HP")

        if acf==1:
            ractanglehp-=50;print("\nTOOK 50 HP")
        elif acf==2:
            ractanglehp-=100;print("\nTOOK 100 HP")
        elif acf==3:
            fanclehp+=20;print("\nHEAL 20 HP")
    if fanclehp<=0:print(f"\n{name} WINS");break
    elif ractanglehp<=0:print("\nFANCLE WINS");break

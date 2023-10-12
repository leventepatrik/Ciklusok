
#bizonyos műveletk ismétlésére való
# ciklusváltozó - számlálja hogy hányszor futott már le a ciklus
# ciklusmag - ismétlendő utasítások
#ciklusfeltétel - itt adjuk meg hofgy meddig fusson a ciklus
def szamlalos_ciklus():

    cv:int = 1

    while(cv < 11):
        print(f" {cv} többé nem kések mert lemaradok fontos információkrol!")
        cv +=1

    print(cv, "a ciklus után")
def elotesztelos_ciklus():


    szam:int=int(input("Adjon meg egy 10-nél nagyobb számot"))
    while szam <= 10 :
        print("10-nél nagyobb számot!")
        szam: int = int(input("Adjon meg egy 10-nél nagyobb számot"))

    print("Hurrá végre sikerült 10 -nél nagyobbat!",szam)


# készíts külön eljárást
# 1. írd ki a számoat a képernyőre 1 és 10 között egymás mellé
def szam_1_10():
     szam:int =1
     while szam <= 10 :
         print(f"{szam}",end= ",")
         szam += 1
#szam_1_10()




# 2. írd ki a számokat 20 és 30 között a képernyőre
def szam_20_30():
    szam1:int = 21
    while szam1 <= 29 :
        print(f"{szam1}",end=",")
        szam1 += 1
#szam_20_30()




# 3. írd ki a 15 és 25 közötti páros számokat
def parosszamok():
    szam2:int =16
    while(szam2 <=25):
        if szam2 % 2 ==0:
            print(f"{szam2}",end=";")
        szam2 += 1
#parosszamok()




#4, írd ki a számokat egyesével 12 és 30 között fordított sorrendben
def fordított():
    szam3:int = 29
    while (szam3 >=11):
        print(f"{szam3}",end=";")
        szam3 -= 1
fordított()











print("hello this ist the to-do list ther is a anime watsh-list and an fall bucket-list"
" and an sieres/film watsh-list and obviously an to-do list")
todolist=["to-do-list":[],"anime-to-watsh-list":[],"series-to-watsh-list":[],"film-to-watsh-list":[],"fall bucket-list":[]]
answerlist=["yes","no"]
addtolist=input("is the to-do-list not in the list then writte yes it in or writte no")
while True :
    if addtolist == answerlist[0] :
        whichlisttoadd=input("please writte the list name")
        if whichlisttoadd not in todolist:
            todolist[whichlisttoadd]=[]
            print( f" list "{whichlisttoadd}" was atatched")
        else :
            print("this list already exist ")
        x=1
        while x==1:
            plus = input ("do you want to add a new list ")
            if plus==answerlist[1]:
                whichlisttoadd=input("please writte the list name")
                todolist.append(whichlisttoadd)
            elif plus==answerlist[1]:
                x=2
    elif addtolist == answerlist [1]:
        break
    while True:
        listworkon=input ("which list do you want to work on ")
        if listworkon in todolist :
            while True:
                listwork =input(f"Gib ein TO-DO für {todolist} ein oder stop zum Beenden ")
                if listwork()=="stop" :
                    break
                todolist.append(listworkon)
                print(f"Aktueller Inhalt von {listworkon}:{todolist}")
            break
        else:
            print("Diese Liste existiert nicht. Bitte wähle eine aus der Übersicht.")
                    
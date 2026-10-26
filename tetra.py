import random
sidequestlist = ["run /walk a shape","draw a person","programm a rock paper sisor game",
                 "win a round of chess against someone ","do your homework","learn for a Test or class test",
                 " clean your room","learn the history of a country","learn to nitt","learn the political situation of a country",
                 "learn basic phrases of a new language","learn all the kinds of sports there is",
                 "learn a new fact about the police ","draw in a new art style","learn how to make shope",
                 "learn how mirrors are made","bouts are made","sowe something","write what you did today",
                 "try remmembering what you did to today a week ago","read a chapter of the book you are corrently reading",
                 "find out why we smell and from what some smells come from","learn everything about one topic in history"
                 ]

answers=["yes","no"]
print("hello")
print ("Hello this is the sidequest generator which generates sidequests for you. " \
"Do not worry every sidequest is explained and even dull ones are made interessting." \
"After every one you either send a quick picture or we will track it our selves. " \
"For those you can not do or wich not to you can skip per day you only how up to 10 skips. ")
random_index=random.randint(0,len(sidequestlist)-1)
random_sidequest=sidequestlist[random_index]
repeat=0
question_again= 0
while question_again == 0:
    while repeat<=15:
        random_index=random.randint(0,len(sidequestlist)-1)
        random_sidequest=sidequestlist[random_index]
        print (random_sidequest)
        ask=input("do you agree to do this sidequest?:")
        if ask == answers[0]:
            print (" very well good luck")
            finished = input("have you completet the sidequest if yes here comes te next if no continue")
            if finished == answers[0]:
                question_again=0
                repeat=0

        elif ask == answers [1]:
            yousure=input("are you sure if yes than we will give you a new task if no please comlete the sidetask")
            if yousure == answers[1]:
                repeat = repeat+1
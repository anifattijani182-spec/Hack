import streamlit as st


import random
wordlist=["yes","YES"]
def checkinganswers_POS_G ():
   global random_index
   global q
   global question
   global wordlist
   global x 
   if random_index == 0 :
      if  q== 0  :
         print (" correct ")
         question= input ("do you want another Tsk for the same topic answer yes or no")
         if question==wordlist[0 or 1] :
            x=0
         else:
            x=1
      elif q >0 or q <=0 :
         print ("incorrect")
         question= input ("do you want another Tsk for the same topic answer yes or no")
         if question==wordlist[0 or 1] :
            x=0
         else:
            x=1   
   if random_index == 1: 
      if  q== 4  :
         print (" correct ")
         question= input ("do you want another Tsk for the same topic answer yes or no")
         if question==wordlist[0 or 1] :
            x=0
         else:
            x=1         
      elif q >4 or q <=4 :
         print ("incorrect")
         question= input ("do you want another Tsk for the same topic answer yes or no")
         if question==wordlist[0 or 1] :
            x=0
         else:
            x=1   
   if random_index == 2: 
      if  q== 2  :
         print (" correct ") 
         question= input ("do you want another Tsk for the same topic answer yes or no")
         if question==wordlist[0 or 1] :
            x=0
         else:
            x=1 
      elif q >2 or q <=2:
         print ("incorrect") 
         question= input ("do you want another Tsk for the same topic answer yes or no")
         if question==wordlist[0 or 1] :
            x=0
         else:
            x=1  
   
 
           
x=0               
topicgraphposition=[" a graph has the f(X)=x²+2"," a graph has the f(X)=2x²"," a graph has the f(X)=(x-2)²"]
chemvoc=["Methan","Ethan","Propan","Butan","Pentan","Hexan","Heptan","Octan","Nonan","Decan","Hexadecan","Octadecan"]
chemvoc2=["CH4","C2H6","C3H8","C4H10","C5H12","C6H14","C7H16","C8H18","C9H20","C10H22","C16H34","C18H38"]
print("hello Iam tamara")
subject=int(input("what do you want to learn, for math press 0 for chemistry 1 for Physiks 2 for IMP Math 3 "))

quiz_pairs=list(zip(chemvoc,chemvoc2))
random.shuffle(quiz_pairs)
score= 0

if subject == 0 :                                                                                                 #to determain which subject is going to be learnd 
   topic=int(input("wich topic do you want to learn for graphs positioning 0 "))
   while x ==0:
      if topic== 0:                                                                                                  #to determain which topic of the chossen subject is going to be learnd
         print("so graphs position is what you which to learn lets start")
         random_index=random.randint(0,len(topicgraphposition)-1)
         random_topicgraphposition=topicgraphposition[random_index]
         print("Task:1" )
         print(random_topicgraphposition)
         q=int(input("where is it positioned now is it 2 to the y-Achse prsse 0 or -2 to the y-achse 1,2 to the x-achse 2, -2to the x-achse 3,strecket to factor 2 press 4 or still in it start position presse 5 "))
         checkinganswers_POS_G()
      
if subject == 1:
   topic =int(input("which topic do you want to learn for vocabs press 0"))
   while x==0:
      if topic== 0:
         quiz_pairs=list(zip(chemvoc,chemvoc2))
         random.shuffle(quiz_pairs)
         score= 0
         print("so vocabs is what you which to learn lets start")
         print("Task:1" )
         random_index=random.randint(0,len(chemvoc)-1)
         random_chemvoc=chemvoc[random_index]

         for word,correct_chemvoc2 in quiz_pairs :
            print("\n"+ word)
            user_input = input("Your answer : ")
            if user_input.strip().lower()== correct_chemvoc2.lower():                                                #to not diferentiate form writing big or small 
               print("correct")                                                                                      

            else:
               print(f"wrong . the answer was : {correct_chemvoc2}")

import random 
rock= '''       ________
             _/_____[   )
            |/ _____[   )
            |       [   )
            |_______[___)
            
'''
paper='''            _  
                    / |
                ___/  /_____
               |       _____|_
               |       _______|
               |       _____|          
               |__________|

'''
sisor='''       ___________    
               | \  \  ____|_
               |  \  \ ______|
               |   \_[____)
               |_____[____)

'''
lbig='''       ________
             _/_____[   )
            |/ _____[   )
            |       [   )
            |_______[___)
            
''',
'''                  _  
                    / |
                ___/  /_____
               |       _____|_
               |       _______|
               |       _____|          
               |__________|

''',
'''             ___________    
               | \  \  ____|_
               |  \  \ ______|
               |   \_[____)
               |_____[____)

'''




list=["rock","paper","sicor"]
print (" wellkomme to the rock paper sicor game in which you play against a robot ")
userinput= int(input("which one of the following are you chossing rock 0 paper 1 sicor 2"))

if userinput == 0:
        print("you chosse") 
        print(list[0])
        print(rock)
        random_index=random.randint(0,len(lbig)-1)
        random_list=lbig[random_index]
        print("robo chosse")
        print (list[random_index])
if userinput == 1:
        print("you chosse") 
        print(list[1])
        print(paper)
        random_index=random.randint(0,len(lbig)-1)
        random_list=lbig[random_index]
        print("robo chosse")
        print (list[random_index])
if userinput == 2:
        print("you chosse") 
        print(list[2])
        print(sisor)
        random_index=random.randint(0,len(lbig)-1)
        random_list=lbig[random_index]
        print("robo chosse")
        print (list[random_index])
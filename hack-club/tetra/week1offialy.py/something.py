spielfeld1 = [" "," "," "]
spielfeld2 = [" "," "," "]
spielfeld3 = [" "," "," "]


def spielfeld_ausgeben():
    print (spielfeld1)
    print (spielfeld2)
    print (spielfeld3)

stichwort = ["O","X"]
spielfeld_ausgeben
werspielt=int(input("who plays first X 1, O 2"))

if werspielt == 1:
    X=1
else:
    X= 2
spielfertigX1= ["X","X","X"]
spielfertigX2= ["X"," "," "]
spielfertigX3= [" ","X"," "]
spielfertigX4= [" "," ","X"]

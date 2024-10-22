'''
1 for snake 
-1 for water 
0 for gun

'''
import random 
computer= random.choice([-1,1,0])
youStr =(input(" Enter your choice\ns for snake\ng for gun\nw for water:\t"))
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}

you=youDict[youStr]

print(f"You chose {reverseDict[you]},Computer chose {reverseDict[computer]}")
if (computer==you):
    print ("It's a draw")
else:
    if(computer==1 and you==0):
        print("You won")
    elif(computer==-1 and you==0):
        print("Computer won")
    elif(computer==0 and you==1):
        print("Computer won")
    elif(computer==0 and you==-1):
        print("You won")
    elif(computer==-1 and you ==1):
        print("Computer won")
    elif(computer==-1 and you==1):
        print("You won")



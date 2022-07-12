import random
d=[1,2,3,4,5,6]


while True:
    
    
    x=input("enter y to roll a die or to stop enter n:")
    if(x=='y' or x=='Y'):
        op=random.choice(d)
        print("The Outcome after rolling a die is->",op)
        
    elif(x=='n' or x=='N'):
        print("Now the rolling of die is stopped")
        print("Thanks for rolling the die 😁😁😁")
        break
    else:
        print("NOT VALID😝😝 😝 PLEASE CHECK AGAIN")
        

    if(op==1):
        print(' _ _ _ _ _ _ \n'
              '|           |\n'  
              '|           |\n'
              '|     O     |\n'
              '|           |\n'
              '|_ _ _ _ _ _|\n')
    elif(op==2):
         print('_ _ _ _ _ _ _\n'
              '|           O|\n'  
              '|            |\n'
              '|            |\n'
              '|            |\n'
              '|O_ _ _ _ _ _|\n')
    elif(op==3):
         print('_ _ _ _ _ _ _ \n'
              '|          O |\n'  
              '|            |\n'
              '|     O      |\n'
              '|            |\n'
              '|O_ _ _ _ _ _|\n')
    elif(op==4):
        print(' _ _ _ _ _ _ _\n'
              '|O           O|\n'  
              '|             |\n'
              '|             |\n'
              '|             |\n'
              '|O_ _ _ _ _ _O|\n')
    elif(op==5):
        print(' _ _ _ _ _ _ _\n'
              '|O           O|\n'  
              '|             |\n'
              '|      O      |\n'
              '|             |\n'
              '|O_ _ _ _ _ _O|\n')
    elif(op==6):
         print('_ _ _ _ _ _ _ _\n'
              '|O           O|\n'  
              '|             |\n'
              '|O           O|\n'
              '|             |\n'
              '|O_ _ _ _ _ _O|\n')
          
         
              

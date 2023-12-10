import classes

def ValidateName(name):
    return len(name) > 3 
  
player_name = input("Enter name : ")

if validate_name(player_name):
    print(f'Welcome to the "Who is in the festive spirit!"{player_name}')
    
else:
    print("INVALID: You need to enter numbers with more than 3 letters!")

         
validate_name()
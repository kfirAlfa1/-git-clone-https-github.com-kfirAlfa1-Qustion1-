#Kfir Alfandary
# Qustion number 2

def sum_Of_Num(): 
    userInput = input("Please enter input:") 
    sumOfNum=0
    while (userInput !="stop"):
        if (userInput.isnumeric()):
             sumOfNum=sumOfNum+(int(userInput))
             
        userInput = input()
    return("The total sum of the numbers that you insert is : "+str(sumOfNum)) 
      
print(sum_Of_Num())
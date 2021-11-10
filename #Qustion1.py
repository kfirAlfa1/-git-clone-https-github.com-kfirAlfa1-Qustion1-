#Kfir Alfandary
#Qustion number 1

num_List = [0, 1, 2, 3, 4, 5, 6, 7 ,9] 

def missing_Num(num_list):   
	sumOfInputList=sum(num_list)  
	maxSum=sum(range(0,10))
	return(maxSum-sumOfInputList)
	  
print(missing_Num(num_List))
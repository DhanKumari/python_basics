#def printf(message,message1): # Required argument
#def printf(message,message1="second"):  # Default argument 
def printf(*messages):  # Variable length argument   
    #print(messages)
    for message in messages:
        print(message)
  
#printf(message1="first", message="second") 
# Calling the function
#Keyword argument

printf("kannu","dhan","kc","kartik")


def sum(*n):
    r = 0
    for i in n:
        r+=i
    return r

re=sum(1,2,3,4)
print(re)


#lambda  anonymous function .. one line code 
sobb = lambda x,y: x-y
print(sobb(9,5))

# How to create a functionn that passes data

# step 1> create a fuinction defintion
def bnbrefund(username, RefundAmount):
    print('sorry'+ username + 'for youur canellation')     
    print(' we will refund $' + RefundAmount+'amount to yourbank. ') 
# step2. call the function/ excute instruction 
# bnbrefund('jacob', '3000') 

def bday(name,bday):
    print ("my name is " + name + " and my bday is " + bday)

# bday('jahleil', 'march 1') 

def moneyconverter(dollar):
    pennies= dollar * 100
    print('my ' + str(dollar) + 'dollar(s) is equal to ' + str(pennies) + '   pennies.')
   
# moneyconverter(50) 

def areaoftriangle(length, width):
    triangle = length * width * 0.5
    print('area')
    print(triangle)

#areaoftriangle(10,30)

def calculatethearea(length, width, height):
    area = 20*15*23 
    print('Calculate')
    print(area) 

calculatethearea(20,10,23)
   


def fahrenheitconverter(far):
    cel= far - 32 * 5/9
    print('my cel is : ' + str(far))
fahrenheitconverter(32)  




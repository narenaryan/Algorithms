#Greedy method implementation for Indian Currency Returning Machine
#Author: Naren Aryan 18-03-2015
 
#All possible Indian currency
drawer = [1000,500,100,50,20,10,5,2,1]
#calculate change to be returned
change =  abs(int(raw_input('Enter Charge amount: ')) - int(raw_input('Enter customer cash: ')))  
payed = []

#Greedy Algorithm , how simple!
for coin in drawer:
    #Until change is exhausted 
    while change >= coin:
        #remove coin value from change
        change = change - coin
        #Add it to payed record
        payed.append(coin)

#Boom Algorithm completed,wondering

print ' + ' . join(['%d => %d ruppes'%(payed.count(i),i) for i in  sorted(set(payed))[::-1]])

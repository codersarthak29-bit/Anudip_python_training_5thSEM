#program to make atm transasction history 
transactions=[5000,-2000,3000,-1000,-500,7000]
sum=0
larg_dep=transactions[0]
larg_with=transactions[0]
for i in transactions:
    if larg_dep<i:
        larg_dep=i
    if larg_with>i:
        larg_with=i
    sum=sum+int(i)
print("Current Balance:",sum)
deposit=[]
withdrawals=[]
for i in transactions:
    if i>0:
        deposit.append(i)
    else:
        withdrawals.append(i)
print("Deposits: ",deposit)
print("Withdrawals: ",withdrawals)
print("Largest Deposit: ",larg_dep)
print("Largest withdrawal: ",larg_with)



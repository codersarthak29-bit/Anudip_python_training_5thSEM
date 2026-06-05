#program to make a inventory manager stores stock quantites
stock=[25,5,0,12,3,18,0,30]
out_of_stock=0
aval=0
restock=[]
healthy=[]
for i in stock:
    if i==0:
        out_of_stock+=1
    if i<10:
        restock.append(i)
    if i!=0:
        aval+=1
    if i>=15:
        healthy.append(i)
print("Out of Stock: ",out_of_stock)
print("Restock Required: ",restock)
print("Available: ",aval)
print("Healthy Stock: ",healthy)
        
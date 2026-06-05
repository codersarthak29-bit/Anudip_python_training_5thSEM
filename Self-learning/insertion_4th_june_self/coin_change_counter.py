#program to make coin change counter
#given an amount ,determine the minimum number of notes required using 500,200,100,50,20,10
amount = int(input("Enter amount: "))

if amount >= 500:
    count = amount // 500
    print("500 x", count)
    amount = amount % 500

if amount >= 200:
    count = amount // 200
    print("200 x", count)
    amount = amount % 200

if amount >= 100:
    count = amount // 100
    print("100 x", count)
    amount = amount % 100

if amount >= 50:
    count = amount // 50
    print("50 x", count)
    amount = amount % 50

if amount >= 20:
    count = amount // 20
    print("20 x", count)
    amount = amount % 20

if amount >= 10:
    count = amount // 10
    print("10 x", count)
    amount = amount % 10
print("And ",amount,"rupees")
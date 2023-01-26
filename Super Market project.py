from datetime import datetime

name=input("Enter your name:")
# List of items
list='''
wheatflour        Rs 45/kg
moong dal         Rs 55/kg
Red gram          Rs 120/kg
Gold drop oil     Rs 150/liter
Dabur Red paste   Rs 175/each
Maggie            Rs 90/each 
Rice              Rs 50/kg
Santoor soap      Rs 200/pack
Almonds           Rs 450/kg
'''
# Declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

# Rates of items
items={'wheatflour':45,
'moong dal':55,
'Red gram':120,
'Gold drop oil':150,
'Dabur Red paste':175,
'Maggie':90,
'Rice':50,'Santoor Soap':200,'Almonds':450}
option=int(input("for list of items press 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*6)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","VINEETHA Super Market",25*"=")
            print(28*" ","WANAPARTHY")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',ilist[i],8*' ',qlist[i],3*' ',plist[i])
            print(75*"-")
            print(50*"",'totalamount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(50*" ","THANK YOU VISIT AGAIN")
            print(75*"-")
            
        












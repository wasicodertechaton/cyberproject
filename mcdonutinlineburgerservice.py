#MAC DONUTS ONLINE FOOD SERVICE FOR SELLING BURGERS ONLY ONLY BURGERS
print("MAC DONUTS PRO OFFERS🍕🍕🍕🍔🍔🍔🍟🍟🍟")
print("-----------------------------------------------")
print("MAC DONUTS PRO OFFERS🍕🍕🍕🍔🍔🍔🍟🍟🍟 ONLINE SERVICES")
print("-----------------------------------------------------")
print("BURGERS CATEGORY🍔")
print("---------------------")
print("🥟🍔cheese burger,press A for the burger COST:400$")
print("🍗🍔chicken burger,press B for chicken burger COST:250$")
print("🥚🍔egg burger,press C for that burger COST: 120$")
print("🥚🥚🍔double egg burger,press d for double egg burger COST: 170$")
print("-------------------------------------------------")
z=str(input("enter A,B,C OR D:"))
y=int(input("quantity:"))
a=(400)
b=(250)
c=(120)
d=(170)
zz=(60)
a1=(400)*(y)+zz
a2=(250)*(y)+zz
a3=(120)*(y)+zz
a4=(170)*(y)+zz
print("-----------------------------------")
if z==("a"):
    print("note delivery price may also be included")
    print(" your your total bill is =",a1)
    print("your order is cheese burger and final cost with order=",a1)
    print("the delivery price=",zz)
    print("-----------------------------------")
    print("TOTAL=",a1,"$")
elif z==("b"):
    print("note delivery price may also be included")
    print(" your your total bill is =",a2)
    print("your order is cheese burger and final cost with order=",a2)
    print("the delivery price=",zz)
    print("-----------------------------------")
    print("TOTAL=",a2,"$")
elif z==("c"):
    print("note delivery price may also be included")
    print(" your your total bill is =",a3)
    print("your order is cheese burger and final cost with order=",a3)
    print("the delivery price=",zz)
    print("-----------------------------------")
    print("TOTAL=",a3,"$")
elif z==("d"):
    print("note delivery price may also be included")
    print(" your your total bill is =",a4)
    print("your order is cheese burger and final cost with order=",a4)
    print("the delivery price=",zz)
    print("-----------------------------------")
    print("TOTAL=",a4,"$")
else:
 print("choose from option A B C OR D if not THAN THANK YOU!")
 
     
    

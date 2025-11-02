print("=========================================")
print("      welcome to hamayoon resturant      ")
print("=========================================")
print("NO  |   FOOD ITEM     |          PRICE af")
print("=========================================")
print("1   | chicken biryani |          250  AFN")
print("2   | kabuli pulao    |          300  AFG")
print("3   | muntoo          |          400  AFG")
print("4   | kabab           |          200  AFG")
print("5   | bread           |          10   AFG")
print("=========================================")
choice= input("enter your choice")
if choice=="1":
    print("your order is chiken biryani.")
elif choice=="2":
    print("your order is kabuli pulao.")
elif choice=="3":
    print("your order is muntoo.")
elif choice=="4":
    print("your order is kabab.")
elif choice=="5":
    print("your order is bread.")
else:
    print("your order is not accepet.")
    print("please try again.")
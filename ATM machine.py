print("Welcome to ATM ")
restart = ("Y")
chances = 3
balance = 990.12
while chances>=0:
    pin = int(input("please enter your 4 digit pin :"))
    if pin==1234:
        print("you entered your pin correctly")
        print("please press 1 for ypour balance")
        print("please press 2 to make withdrawl")
        print("please press 3 to pay in")
        print("plese press 4 to return card\n")

        option = int(input("what would like to choose :"))
        if option==1:
            print("your balance is $",balance)
            restart = input("would you like to go back :")
            if restart in ("no","No","n""N"):
                print("Thank You")
                break
        elif option==2:
             option2 = ("Y")
             withdrawl = float(input("how much would you like to withdrawl : "))
             if withdrawl in [10,20,40,60,80,100]:
                 balance = balance-withdrawl
                 print("\n your balance is $", balance)
                 restart = input("would you like to go back : ")
                 if restart in ("no", "No", "n""N"):
                     print("Thank You")
                     break
             elif withdrawl!=[10,20,40,60,80,100]:
                 print("invalid amount, please try again\n")
                 restart = ("y")
             elif withdrawl==1:
                 withdrawl = float(input("please enter desired amount :"))
        elif option==3:
            pay_in = float(input("how much would you like to pay in :"))
            balance = balance+pay_in
            print("\n your balance is $", balance)
            restart = input("would you like to go back :")
            if restart in ("no", "No", "n""N"):
                print("Thank You")
                break
        elif option ==4:
            print("please wait whenever your card is not returned  ")
            print("Thank You For Your service")
            break
        else:
            print("please enter a correct number")
            restart ("y")
    elif pin!=1234:
        print("incorrect password")
        chances =  chances - 1
        if chances == 0:
            print("no more tries")
            break



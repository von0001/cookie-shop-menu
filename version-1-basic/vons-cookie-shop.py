def ShopChoices():
    print("Welcome to the Cookie Shop!")
    print("1 - Buy Cookies ($2.50 each)")
    print("2 - Check Current Total")
    print("3 - Reset Order")
    print ("4 - Exit")
    userInput = int(input("Pick an option."))
    while userInput < 1 or userInput > 4:
            userInput = int(input("That is an invalid entry. Please enter a valid choice."))
    else:
         if userInput >= 1 and userInput <= 4:
              return userInput

def AddCookies(total):
        cookies = int(input("How many cookies would you like?"))
        total += cookies * 2.50
        return total
     
def CurrentTotal(total):
     print(f"Your total is ${total:.2f}")

def ResetOrder(total):
     total = 0
     print(f"Your total is ${total}")
     return total

total = 0

while True:
     userInput = ShopChoices()
     
     if userInput == 1:
          total = AddCookies(total)
     elif userInput == 2:
          CurrentTotal(total)
     elif userInput == 3:
          total = ResetOrder(total)
     elif userInput == 4:
          print("Thank you for visiting!")
          break

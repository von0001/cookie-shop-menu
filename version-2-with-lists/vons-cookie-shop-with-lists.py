## modules

def vonTracker():
    print("Welcome to the von's Cookie Order Tracker! Here's your options.")
    print("[1] - Add Cookie To Order")
    print("[2] - View Current Order")
    print("[3] - Reset Order")
    print("[4] - Exit")
    userInput = int(input("What would you like to do?"))
    while userInput < 1 or userInput > 4:
            userInput = int(input("That is an invalid entry. Please enter a valid choice."))
    else:
         if userInput >= 1 and userInput <= 4:
              return userInput

def addCookie():
    cookies = str(input("What are the names of the cookies you'd like to add?"))
    cookieList.append(cookies)
    return cookieList

def viewOrder():
     print("Here’s your current order:")
     for cookies in cookieList:
          print(f"- {cookies}")

def resetOrder():
    cookieList.clear()

## variables

cookieList = []

#actual code

while True:
      userInput = vonTracker()

      if userInput == 1:
          addCookie()
      elif userInput == 2:
          viewOrder()
      elif userInput == 3:
          resetOrder()
      elif userInput == 4:
          print("Thank you for using von's Cookie Tracker!")
          break

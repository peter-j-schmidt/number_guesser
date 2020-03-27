import random

random_number = random.randint(0, 10)

user_input = ''

count = 0

while (count < 10):
     print("You have 10 tries to guess the computer's number.")
     user_input = input("Enter a number between 1 and 10: ")
     if user_input.isdigit() == False:
         print("That's not a valid number...")
     else:
         user_input = int(user_input)
         if user_input > 10:
             print("That number is too high!!!!")
         else:
             if user_input != random_number:
                 count += 1
                 if count < 9:
                    print("Wrong! You only  have {} more tries!".format(10 - count))
                 elif count == 9:
                    print("Wrong! You only have 1 more try!")
                 elif count == 10:
                     print("Wrong! You've lost. Try again next time!")
             else:
                 print("Congrats! You've won!")
                 break;

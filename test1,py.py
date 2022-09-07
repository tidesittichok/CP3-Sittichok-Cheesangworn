# correctNumber = 76
# userGuess = 0
# while userGuess != correctNumber:
#     userGuess = int(input("Please guess a number : "))
#     if userGuess < correctNumber:
#         print("Lower than correct number !!")
#     elif userGuess > correctNumber:
#         print("Higher than correct number !!")
#     elif userGuess == correctNumber:
#         print("Correct Number!!!!")
# -----------------------------------------------


# usernameInput = input("Username : ")
# passwordInput = input("Password : ")
#
# while usernameInput != "admin" or passwordInput != "1234":
#     usernameInput = input("Username : ")
#     passwordInput = input("Password : ")
# print("Done!!!")

# -----------------------------------------------

# inputRound = int(input("Please Enter Number : "))
# sum = 0
# for x in range(inputRound):
#     inputNumber = int(input("x"+str(x+1)+" : "))
#     sum += inputNumber
# print(sum)

# -----------------------------------------------

# result = ""
# start = int(input("Start : "))
# step = int(input("Step : "))
#
# for i in range(5):
#     print(start + step * i,end=" ")
#     result += str(start + step * i + 1)
#
# print(result)

# -----------------------------------------------
# num = int(input("input number : "))
# for x in range(12):
#     print(num,"x",x+1,"=",num*(x+1))

# -----------------------------------------------
# for i in range(12):
#     for x in range(12):
#         print(i+1,"x",x+1,"=",(i+1)*(x+1))
# -----------------------------------------------

# for i in range(12):
#     for x in range(12):
#         print(i+1,"x",x+1,"=",(i+1)*(x+1))
#     break

# -----------------------------------------------

count = int(input("how much * do you want? "))
result = ""
for i in range(count):
    result = "*"*(i+1)
    print(result)

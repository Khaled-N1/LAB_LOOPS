"""
## 2) Using a while loop and input , do the following :
- Ask the the user : "what is the product of 7 * 24 ?"
- check if the answer is right then exit the loop and print "You answered this Question correctly"
- if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
"""

puzzle="what is the product of 7 * 24 ??\n"
while int(input(puzzle)) != 7*24:
    print("Wrong answer Try again !")
else : 
    print("Right answer Good job ! ")  
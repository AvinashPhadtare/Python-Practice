# ALL IMPORTS :-
import random
import time

# CONSTANTS AND VARIABLES:-
OPRATIONS = ["+","-","*"]
MIN_NUM = 1
MAX_NUM = 10
TOTAL_QUESTIONS = 10
valid_choice = 1



print(" +----------- Welcome to MATH quiz -------------+ ")
print("Difficulty Levels :-\n1. Easy\n2. Medium\n3. Hard")
choice = int(input("Enter your choice of number:- "))


if choice == 1:
    MAX_NUM = 10
elif choice == 2:
    MAX_NUM = 20 
elif choice == 3:
    MAX_NUM = 25
else:
    print("You entered a Wrong Choice !...")
    valid_choice = 0



if valid_choice:
    def generate_problem():
        left_no = random.randint(MIN_NUM, MAX_NUM)
        right_no = random.randint(MIN_NUM, MAX_NUM)
        opration = random.choice(OPRATIONS)


        expr = str(left_no)+" "+opration+" "+str(right_no)
        ans = eval(expr)

        return expr, ans
    
    print("\n\t+--------------- Start ----------------+\n")
    start_time = time.time()
    
    for i in range(TOTAL_QUESTIONS):
        expr, ans = generate_problem()

        while True:
            gussed = input("Problem #"+str(i+1)+":- \n\t"+expr+" = ")
            if gussed == str(ans):
                break
            print()

    end_time = time.time()
    total_time = round(end_time - start_time)

    print("\n\t+--------------- Nice Work ! -----------------+")
    print("You finished this QUIZ in", total_time,"seconds !...")

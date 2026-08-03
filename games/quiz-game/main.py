#This is Game about Quiz (In this we ask user some questions and based on your answer we gives them marks for that)
def question(ans,cans):
    if ans.lower()==f'{cans}':
        global score
        score = 0
        print("Correct")
        score += 1
        return score
    else:
        print("Wrong")

print("WELCOME to my Quiz game!")
play = input("Do you want to play?(yes/no): ")
count = 0
if play.lower() == 'no':
    quit()
elif play.lower() == 'yes':
    print("OK! Let's play....")
    ans = input("1] What does CPU stand for?\nAns:")
    cans = 'central processing unit'
    question(ans,cans)
    print('\n')

    ans = input("2] What does GPU stand for?\nAns:")
    cans = 'graphics processing unit'
    question(ans,cans)
    print('\n')

    ans = input("3] What does LLM stand for?\nAns:")
    cans = 'large language model'
    question(ans,cans)
    print('\n')

    ans = input("4] What does AI stand for?\nAns:")
    cans = 'artifical inteligence'
    
    question(ans,cans)
    print('\n')

    ans = input("5] What does RAM stand for?\nAns:")
    cans = 'random access memory'
    question(ans,cans)
    print('\n')

    ans = input("6] What does PSU stand for?\nAns:")
    cans = 'power supply'
    question(ans,cans)
    print('\n')
    if score == 1:
        count+=1
else:
    print("You entered Wrong choice")



print("You got "+str(count)+" Question correct")

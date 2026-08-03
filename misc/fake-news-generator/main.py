import random

subjects = ["Virat kohli","Rohit sharma","Shubhman gill","Sharukh khan","Deepika","Ranveer","Modi ji","Monkey from Mumbai"]

actions = ["launches","eats","riding","swimming","singing","dancing","laughing"]

places = ["in Mumbai's local train","at Red Fort","in Bathroom","at Public Place","at Gateway of India","at Dubai"]


# Function to generate news
def generate_news():
    sub = random.choice(subjects)
    act = random.choice(actions)
    place = random.choice(places)
    return f"BREAKING NEWS: {sub} {act} {place}"


print("\n1. Generate News\n2. Add Word and Generate News\n")
choice = int(input("Enter your choice: "))


# Ask user if they want to save news
save_option = input("Do you want to save news to file? (yes/no): ").strip().lower()


if choice == 1:
    while True:
        headline = generate_news()
        print("\n" + headline)

        # Save to file if user selected yes
        if save_option == "yes":
            with open("Fake_News.txt", "a") as file:
                file.write(headline + "\n")

        user_input = input("\nDo you want another one? (yes/no): ").strip().lower()
        if user_input == "no":
            break
        elif user_input == "yes":
            continue
        else:
            print("Wrong Choice")
            break
            

elif choice == 2:
    print("\nWhat do you want to change?\n1. Subject\n2. Action\n3. Place")
    choice1 = int(input("Enter your choice: "))

    if choice1 == 1:
        add_subject = input("Enter a Subject: ").capitalize()
        subjects.append(add_subject)

    elif choice1 == 2:
        add_action = input("Enter an Action: ").lower()
        actions.append(add_action)

    elif choice1 == 3:
        add_place = input("Enter a Place: ")
        places.append(add_place)

    else:
        print("Wrong choice!")

    while True:
        headline = generate_news()
        print("\n" + headline)

        # Save to file if user selected yes
        if save_option == "yes":
            with open("Fake_News.txt", "a") as file:
                file.write(headline + "\n")

        user_input = input("\nDo you want another one? (yes/no): ").strip().lower()
        if user_input == "no":
            break


else:
    print("You entered wrong choice!")


print("\nThanks for using Fake News Generator!.. Goodbye :)")

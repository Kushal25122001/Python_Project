import random

list1 = ["S","W", "G"]
Com_points = 0
My_points = 0
no_of_chances = 0
print("You have 10 chances to win this battle")

while(no_of_chances < 10) :
    My_choice = input("Enter your choice : s for snake, w for water, g for gun\n")
    Com_choice = random.choice(list1)

    if My_choice == "S" and Com_choice == "S" :
        print("We are draw :")
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
        no_of_chances = no_of_chances + 1
    elif My_choice == "S" and Com_choice == "W" :
        print("Snake drink all the water so I win :")
        My_points = My_points + 1
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
        no_of_chances = no_of_chances + 1
    elif My_choice == "W" and Com_choice == "S" :
        print("Water drink by snake so you win :")
        Com_points = Com_points + 1
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
        no_of_chances = no_of_chances + 1
    if My_choice == "G" and Com_choice == "G" :
        print("We are draw :")
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
    elif My_choice == "S" and Com_choice == "G" :
        print("Snake killed by gun so you win :")
        Com_points = Com_points + 1
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
        no_of_chances = no_of_chances + 1
    elif My_choice == "G" and Com_choice == "S" :
        print("Snake killed by gun so I win :")
        My_points = My_points + 1
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
        no_of_chances = no_of_chances + 1
    if My_choice == "W" and Com_choice == "W" :
        print("We are draw :")
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
    elif My_choice == "W" and Com_choice == "G" :
        print("Water drone the gun so I win :")
        My_points = My_points + 1
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
        no_of_chances = no_of_chances + 1
    elif My_choice == "G" and Com_choice == "W" :
        print("Water drone the gun so you win :")
        My_points = My_points + 1
        print("My points", My_points)
        print("Com points", Com_points)
        print("No of choice is left", 9 - no_of_chances)
        no_of_chances = no_of_chances + 1
    else :
        print ("My points", My_points, "Com points", Com_points)

print("My points", My_points, "Your point", Com_points)
if My_points > Com_points :
    print("I win the battle")
elif My_points < Com_points :
    print("You win the battle")
elif My_points == Com_points :
    print("Draw match : Let's play another round")
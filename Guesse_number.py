''' Take a input from user and print the number of guess is right or wrong which is input by the user according to the
following condition...
limited number of guesses 9
print number of guesses left
game over if no of guesses is finished
no of guesses he took to finished '''

n = 18
no_of_guesses = 1
print("You have a limited no of guesses 9")
while(no_of_guesses <=9) :
    guess_no = int(input("guess the number\n"))
    if guess_no >18 :
        print("you entered greater no please enter smaller no")
    elif guess_no<18 :
        print("you have entered smaller no please enter greater no")
    else :
        print("you own")
        print(no_of_guesses, "no of guesses you took to finish")
        break
    print (9 - no_of_guesses, "no of guesses left")
    no_of_guesses = no_of_guesses + 1

if(no_of_guesses > 9) :
    print("game over")
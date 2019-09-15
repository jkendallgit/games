# Number Guess v1.0.0

print("")
print("-------------------------Welcome To Number Guess!---------------------------------------")
print("In this game, you think of a number from 1 through n and I will try to guess what it is.")
print("After each guess, enter h if my guess is too high, l if too low, or c if correct.")
print("----------------------------------------------------------------------------------------")
print("")

total_games = 0
total_guesses = 0
user_input = int(input ("Please enter a number n: "))
high = user_input
    
play = "y"

while play == "y":
    indicator = ""
    num_guesses = 0
    low = 1
    high = user_input
  
    guess = (low + high) // 2
    num_guesses += 1

    while indicator != "c":
        indicator = input(str(guess) +"? ")
        if indicator == 'c':
            break
           
        elif indicator == 'h':
            if(low + 1 == guess):
                guess = low
                break
            high = guess - 1
            guess = (low + high) // 2
            num_guesses += 1
         
        elif indicator == 'l':
            if(high - 1 == guess):
                guess = high
                break
            low = guess + 1
            guess = (low + high) // 2
            num_guesses += 1
        else:
            print("Invalid Input..Please enter c, h, or l")

    total_guesses = total_guesses + num_guesses
    total_games += 1
    avg_guesses_per_game = round((total_guesses / total_games), 2)
    
    print("Your number is " + str(guess) + ".")
    print("It took me " + str(num_guesses) + " guesses.")
    print ("I averaged " + str(avg_guesses_per_game) + " guesses per game for " + str(total_games) + " game(s).")
    play = input ("Play again (y/n)?: ")
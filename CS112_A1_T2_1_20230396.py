#file :CS112_A1_T2_1_20230396.py.
# purpose: 100 game,Starting at zero, each of the two players adds a number between 1 and 10 to the total in turn.
# The winner is the one who hits 100.
#Author :Marim ali abdelkarim
#ID : 20230396


# Step 1: Set up the game
def game():
    # Welcome to the 100 game of Python!
    print("Welcome to the 100 game of Python!")
    sum = 0
    player = 1

    # Step 2: Create the game loop
    while sum < 100:
        # Step 3: Ask the current player for input
        try:
            num = int(input(f"Player {player}, please choose a number between 1 and {min(10, 100 - sum)}: "))

            if 1 <= num <= min(10, 100 - sum):
                # Step 4: Add the entered number to the sum
                sum += num
                print(f"Sum: {sum}")

                # Step 5: Check if the sum has reached 100
                if sum == 100:
                    # Step 6: Declare the current player as the winner, Print the winner's name and exit the loop
                    print(f"Player {player} wins!")
                    end = input("enter E to exist :")
                    print (end)
                    break

                # Step 7: Switch the current player
                player = 3 - player  # Switch player between 1 and 2
            else:
                # Step 8: Check the validity of the input
                print(f"Invalid input. Please enter a number between 1 and {min(10, 100 - sum)}.")
        except ValueError:
            #  step 9:Handling non-integer input
            print("Invalid input. Please enter a valid integer.")

    # Step 10: Print "Game over!" after the loop ends
    print("Game over!")



# Start the game
game()





from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# Append the stacks to stacks list
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the Game

# Ask the user to choose a number of disks
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:  # If it is lower than 3, ask again
    num_disks = int(input("It has to be greater than or equal to 3\n"))

for size in range(num_disks, 0, -1):  # Loop backward through disks
    left_stack.push(size)  # Push the value to the left_stack

# For towers of hanoi, the optimal moves number is always 2**num_disks - 1.
num_optimal_moves = 2**num_disks - 1  # Calculate the optimal moves number
# Tell the player the fastest he can solve the game
print("\nThe fastest you can solve this game is in {num} moves".format(
    num=num_optimal_moves
))


# Get User Input
def get_input():
    # Create the choices list using the first letter of the name of each stack
    choices = [stack.get_name()[0] for stack in stacks]
    while True:  # Create the game loop
        for i in range(len(stacks)):  # Iterate i through the number of stacks
            name = stacks[i].get_name()  # Get the name of the current stack
            letter = choices[i]  # Set a choice letter to the actual stack
            # Ask the player to enter a letter
            print("Enter {letter} for {name}".format(letter=letter, name=name))
        user_input = input("")  # Get the player's input
        if user_input in choices:  # Check if the input is valid
            for i in range(len(stacks)):  # Iterate i through the len of stacks
                # Check if input is the actual choice
                if user_input == choices[i]:
                    return stacks[i]  # Return the choosen stack


# Play the Game
num_user_moves = 0  # Counter for player's moves

# Looping until all disks are in the right stack
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:  # Loop through stacks
        stack.print_items()  # Print items of each stacks
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()  # Ask the user to choose a stack to move from
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()  # Ask the user to choose a stack to move to
        if from_stack.is_empty():  # Check if the from stack is empty
            print("\n\nInvalid Move. Try Again")
        # Check if to stack is empty or if the value on the top of fromstack
        # is less than the one on the top of to stack
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()  # Pop and get the disk on from stack
            to_stack.push(disk)  # Push the disk to to stack
            num_user_moves += 1  # Increment the user's moves number
            break  # Break from the loop
        else:  # Else, the move is invalid
            print("\n\nInvalid Move. Try Again")

print("\n\nYou did only {user_moves} moves, the best was {optimal_moves} moves"
      .format(user_moves=num_user_moves, optimal_moves=num_optimal_moves))

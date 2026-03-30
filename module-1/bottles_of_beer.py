# Name: Shannon Blake
# Date: March 30, 2026
# Assignment 1.3
# Purpose: Count down bottles of beer on the wall from a user-given number to zero.


def countdown(bottles):
    # Loop while there is more than one bottle remaining
    while bottles > 1:

        # Print the standard verse using the current bottle count
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.")
        print()

        # Decrease the bottle count by one before the next loop
        bottles -= 1

    # Print the final verse using singular "bottle"
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, 0 bottles of beer on the wall.")
    print()


def main():

    # Ask the user how many bottles to start with
    bottles = int(input("How many bottles of beer are on the wall? "))

    # Pass the user's input to the countdown function
    countdown(bottles)

    # Back in main-remind the user to buy more beer
    print("Time to go to the store and buy some more beer!")


# Run the program
if __name__ == "__main__":
    main()

# Importing necessary libraries
import sys  # Provides access to system-specific parameters and functions
import time  # Allows for time-related functions like delays

# Displaying a welcome message
print("\nWelcome Branch - Developer: Mr. Lange")
print("\nWelcome to InfoTechCenter V1.0\n")

# Initializing variables
x = 0  # Counter for loop iterations
ellipsis = 0  # Controls the number of dots in the loading message

# Loop to simulate a system booting animation
while x != 20:
    x += 1  # Increment counter
    message = ("Infotech Center System Booting" + "." * ellipsis)  # Creates loading message with increasing dots
    ellipsis += 1  # Increase ellipsis count
    sys.stdout.write("\r" + message)  # Overwrites the current line in the terminal
    time.sleep(.5)  # Pause for half a second to create the effect

    # Reset ellipsis after reaching 3 dots to loop back
    if ellipsis == 4:
        ellipsis = 0  

    # When the loop completes, display the final message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")

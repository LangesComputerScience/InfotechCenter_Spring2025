# Import necessary libraries
import sys  # Provides access to system-specific parameters and functions
import time  # Allows for time-related functions like delays

# ANSI Escape Sequences for text colors
CYAN = "\033[96m"   # Light Cyan text
GREEN = "\033[92m"  # Light Green text
YELLOW = "\033[93m" # Yellow text
RESET = "\033[0m"   # Resets text color to default

# Displaying a welcome message with color
print(CYAN + "\nWelcome Branch - Developer: Mr. Lange" + RESET)  # Displays developer info in cyan
print(GREEN + "\nWelcome to InfoTechCenter V1.0\n" + RESET)  # Displays system name in green

# Initializing variables for boot-up animation
x = 0  # Counter to control the number of animation cycles
ellipsis = 0  # Tracks the number of dots displayed in the loading message

# Loop to simulate a system boot-up animation
while x != 20:
    x += 1  # Increment loop counter
    message = YELLOW + "Infotech Center System Booting" + "." * ellipsis + RESET  # Displays loading message in yellow
    ellipsis += 1  # Adds dots to the loading message for animation effect
    sys.stdout.write("\r" + message)  # Overwrites the current line in the terminal for a smooth animation
    sys.stdout.flush()  # Ensures immediate update of the output without waiting for a new line
    time.sleep(0.5)  # Pauses for half a second to create a smooth loading effect

    # Reset ellipsis after reaching 3 dots to restart the cycle
    if ellipsis == 4:
        ellipsis = 0  

    # When the loop completes, display the final system access message
    if x == 20:
        print(GREEN + "\n\nOperating System Booted Up - Retina Scanned - Access Granted\n" + RESET)  # Displays success message in green


import random
from time import sleep

# Print a decorative header
print("\n*************************************\n")
print("Weather Branch - Developer: Mr. Lange")

# Dictionary mapping weather conditions to alarm delays and speed limits
WEATHER_IMPACTS = {
    "snowing": {"delay": 30, "speed_limit": 55},
    "blizzard": {"delay": 60, "speed_limit": 45},
    "icy": {"delay": 90, "speed_limit": 35},
    "rainy": {"delay": 10, "speed_limit": 65},
    "windy": {"delay": 5, "speed_limit": 70},
}

def get_weather():
    """Randomly selects and returns a weather condition."""
    return random.choice(list(WEATHER_IMPACTS.keys()) + ["sunny"])

def vehicle_response_system(weather_alert):
    """Prints alarm delay and speed limit based on weather conditions."""
    if weather_alert in WEATHER_IMPACTS:
        impact = WEATHER_IMPACTS[weather_alert]
        print(f"\nThe National Weather Service has updated your alarm by {impact['delay']} minutes because it is {weather_alert} outside.")
        sleep(1)
        print(f"VRS has been engaged, only allowing us to drive {impact['speed_limit']}MPH.")
    else:
        print(f"\nThe National Weather Service is calling for {weather_alert} skies outside.")
        sleep(1)
        print("VRS has been disengaged, drive safe!")

# Execute program
weather_alert = get_weather()
vehicle_response_system(weather_alert)


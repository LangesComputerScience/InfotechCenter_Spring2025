# Print a decorative header
print("\n*************************************\n")
print("Weather Branch - Developer: Mr. Lange\n")

# Import necessary libraries
import random  # Used to randomly select weather conditions
from time import sleep  # Imported but not used in the code

# Function to determine the weather condition
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowing", "blizzard", "icy", "rainy", "windy", "sunny"]
    # Randomly select one condition from the list
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

# Get the current weather alert
weatherAlert = weather()

# Function to adjust alarm based on weather conditions
def vehicleResponseSystem():
    if weatherAlert == "snowing":
        print("\nThe National Weather Service has updated your alarm by 30 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated your alarm by 60 minutes because"
              " it is a", weatherAlert, "outside!")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated your alarm by 90 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated your alarm by 10 minutes because"
              " it is", weatherAlert, "outside.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated your alarm by 5 minutes because"
              " it is", weatherAlert, "outside.")
    else:
        # If the weather is sunny, no alarm adjustment is needed
        print("\nThe National Weather Service is calling for", weatherAlert, 
              "skies outside, drive safe!")

# Call the function to display the appropriate message
vehicleResponseSystem()

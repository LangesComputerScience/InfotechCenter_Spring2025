import random
from time import sleep

# Display program header
print("\n***********************************\n")
print("Gasoline Branch - Developer: Mr. Lange\n")


def gasLevelGauge():
    """Returns a random gas level status."""
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])


def gasStations():
    """Returns a random gas station name."""
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"])


def gasLevelAlert():
    """Checks the gas level and provides an appropriate message based on the fuel status."""

    # Determine the current gas level
    gasLevelIndicator = gasLevelGauge()
    print(f"Current gas level: {gasLevelIndicator}\n")
    sleep(1.25)  # Pause for effect

    if gasLevelIndicator == "Empty":
        # If the tank is empty, give a warning and suggest calling AAA
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        print("Calling AAA...")
    elif gasLevelIndicator in ["Low", "Quarter Tank"]:
        # If gas is Low or at a Quarter Tank, find the closest gas station
        miles_to_gas = round(random.uniform(1, 50) if gasLevelIndicator == "Low" else random.uniform(25.1, 50), 1)
        station = gasStations()  # Get a random gas station
        print(f"Your gas tank is {gasLevelIndicator.lower()}, checking GPS for the closest gas station...\n")
        sleep(1.25)
        print(f"The closest gas station is {station}, which is {miles_to_gas} miles away.")
    else:
        # If gas is Half Tank or higher, reassure the driver
        print(f"Your gas tank is {gasLevelIndicator}. Keep driving safely!")


# Run the gas level alert function
gasLevelAlert()

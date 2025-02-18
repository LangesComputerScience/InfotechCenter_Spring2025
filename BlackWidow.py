import random
from time import sleep

print("\n***********************************\n")
print("Gasoline Branch - Developer: Mr. Lange\n")

def gasLevelGauge():
    return random.choice(["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"])

def gasStations():
    return random.choice(["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees"])

def gasLevelAlert():
    gasLevelIndicator = gasLevelGauge()  # Store the gas level once
    print(f"Current gas level: {gasLevelIndicator}\n")
    sleep(1.25)

    if gasLevelIndicator == "Empty":
        print("****WARNING - YOU ARE OUT OF GAS****\n")
        print("Calling AAA...")
    elif gasLevelIndicator in ["Low", "Quarter Tank"]:
        miles_to_gas = round(random.uniform(1, 50) if gasLevelIndicator == "Low" else random.uniform(25.1, 50), 1)
        station = gasStations()  # Store gas station choice once
        print(f"Your gas tank is {gasLevelIndicator.lower()}, checking GPS for the closest gas station...\n")
        sleep(1.25)
        print(f"The closest gas station is {station}, which is {miles_to_gas} miles away.")
    else:
        print(f"Your gas tank is {gasLevelIndicator}. Keep driving safely!")

gasLevelAlert()
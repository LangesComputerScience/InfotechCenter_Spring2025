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

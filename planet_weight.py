weight = int(input("Put your weight:\n--->"))
planet = str(input("Set the planet destination:\n--->")).lower()

def planet_weight(planet):
    if planet == "mercury":
        gravity = 0.38
    elif planet == "venus":
        gravity = 0.91
    elif planet == "mars":
        gravity = 0.38
    elif planet == "jupiter":
        gravity = 2.53
    elif planet == "saturn":
        gravity = 1.07
    elif planet == "uranus":
        gravity = 0.89
    elif planet == "neptune":
        gravity = 1.14
    else:
        gravity = 0
    return gravity
destination_weight = weight * planet_weight(planet)

print(f"Your weight in {planet.title()} will be: {destination_weight}_")

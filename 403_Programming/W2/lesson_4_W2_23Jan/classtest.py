class Robot:
    def __init__ (self, name, colour):
        self.name = name
        self.colour = colour

robot3 = Robot("Robo3", "green")
print(f"Robot Name: {robot3.name} Robot Colour: {robot3.colour}")


class Rock:
    def __init__ (self, name, colour, madeof):
        self.name = name
        self.colour = colour
        self.madeof = madeof


malachite = Rock("Malachite", "Veridian", "Copper")
print (f"Rock Name: {malachite.name}, Rock Colour: {malachite.colour}, What is it made of? {malachite.madeof}.")


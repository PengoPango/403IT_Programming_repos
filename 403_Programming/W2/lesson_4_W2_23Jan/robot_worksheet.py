class Robot:
    def __init__(self, name, type, power, health):
        self.name = name
        self.type = type
        self.power = power
        self.health = health
    
    def say_hello(self):
        print(f"Hello! My name is {self.name} and I am {self.type}, I have {self.health}HP, and my power level is {self.power}.")

    def charge(self):
        self.power += 10
        print(f"{self.name} is charging! Power level is now {self.power}.")
        if self.power == 100:
            print (f"{self.name} has reached 100 Power level!")
            
    def fight(self, other_robot):
        print (f"\n{self.name} VS {other_robot.name}!!!")
        if self.power > other_robot.power:
            print(f"{self.name} wins the battle!")
            other_robot.health -= 10
            print(f"{other_robot.name} has lost 10HP, they now have {other_robot.health}HP")
        elif self.power < other_robot.power:
            print(f"{other_robot.name} wins the battle!")
            self.health -= 10
            print(f"{self.name} has lost 10HP, they now have {self.health}HP")
        else:
            print("It's a tie!")


robotstocker = Robot("RoboStocker", "Retail-Bot", 40, 30)
robottradesworker = Robot("TradesBot", "Electrician-Bot", 50, 40)
robotyson = Robot ("RoboTyson", "Boxer-Bot", 999, 100)
robotcaretaker = Robot ("RoboTaker", "Caretaker-Bot", 50, 20)

robotstocker.say_hello()
robottradesworker.say_hello()
robotcaretaker.say_hello()
robotyson.say_hello()
print("Im the most viscous, theres never been a champion like me, Im Sonny Liston, Im Jack Dempsey")

print ("\n")

robotstocker.charge()
robotstocker.charge()
robotstocker.charge()
robotstocker.charge()

robottradesworker.charge()
robottradesworker.charge()


robotstocker.fight(robotyson)

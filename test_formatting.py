""" This Module defines a simple robot class and demonstrates its usage. """


class Robot:
    """ Simple robot class than can greet with its name. """

    def __init__(self, name):
        self.name = name

    def greet(self):
        """ Prints a greeting message with the robot's name. """

        print("Hello, I am " + self.name)


myRobot = Robot("Chitti")
myRobot.greet()

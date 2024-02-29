class Mobile:
    def __init__(self, number) -> None:
        self.number = number
        pass

    def turn_on(self):
        print(f"Mobile phone {self.number} is turned on...")

    def turn_off(self):
        print(f"Mobile phone {self.number} is turned off...")

    def call(self, number):
        print(f"Calling {number}...")
    
if __name__ == "__main__":
    mobile_1 = Mobile("01632-960012")
    mobile_1.turn_on()
    mobile_2 = Mobile("01632-960013")
    mobile_2.turn_on()
    mobile_1.call("555-34343")
    mobile_1.turn_off()
    mobile_2.turn_off()

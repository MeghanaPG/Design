class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # different type of slots 
        self.empty = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        # If there is a space available we will allocate the space
        # and return True 
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            return True 


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
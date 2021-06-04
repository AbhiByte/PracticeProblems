class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """

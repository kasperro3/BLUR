
#########################################
# Current data transmistion protocol?
# Throttle;Steering;State;...
##########################################

class Data():
    def __init__(self):
        self.__throttle = 0
        self.__steering = 100
        self.__state = 'S'
    
    def SetThrottle(self, throttle: int):
        if type(throttle) is not int:
            throttle = 0
        elif throttle > 100:
            throttle = 100
        elif throttle < 0:
            throttle = 0
        else:
            self.__throttle = throttle

    def Encode(self) -> str:
        return '';

    # decodes string received from the car
    def Decode(self, data: str) -> dict:
        somedata = 0

    
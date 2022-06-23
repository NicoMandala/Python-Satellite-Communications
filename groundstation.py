class Antenna:
    """Instatiate a ground station with all its parameters
    Gain,EIRP, Usable Frequencies, Efficiencies, Dish Diameter"""

    def __init__(self,dia,EIRP,eta,freq):
        self.dia = 70 # diameter
        self.EIRP = 1000 # effective isotropic radiated power
        self.freq = 27*10^9 # frequency used in the radar
        self.eta = 0.55 # overall efficiency of the radar

    def Gain(self):
        return 10*log10(self.eta*(pi*self.dia*self.freq/c)^2)


class Groundstation:
    # Ground stations are defined based on three parameters latitude, longitude and height
    # Possible ideas for next versions: choose the central body
    def __init__(self,lat,long,height):
        self.lat = 0
        self.long = 0
        self.height = 0
from numpy import log10, pi

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
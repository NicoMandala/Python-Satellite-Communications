from numpy import log10, pi

class Antenna:
    """Instatiate a ground station with all its parameters
    Gain,EIRP, Usable Frequencies, Efficiencies, Dish Diameter"""

    def __init__(self,dia,EIRP,eta,freq):
        self.dia  = dia # diameter
        self.EIRP = EIRP # effective isotropic radiated power
        self.freq = freq # frequency used in the radar
        self.eta  = eta  # overall efficiency of the radar


# Gain definition 
# diameter

    def Gain(self):
        return 10*log10(self.eta*(pi*self.dia*self.freq/c)^2)

    

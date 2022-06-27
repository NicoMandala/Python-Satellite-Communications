# This is the beginning of the python library for ground station on Luna
# Copyright (c) 2022 Chaitanya Mandala 
# 
# All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# Step 1: Antenna parameters
# Step 2: Processing received telecommunication data
# Step 3: Transmit the data

# possible name: pylinkluna , 
# inspirations: pylink, nasa ground-station library
# guide: Durante and his team


# Design philosophy : UI must
# Use of classes like properties with default values like ground station
# Ground station properties Gain, EIRP, Polarisation, power flux density



from numpy import log10, pi

global c

c = 3*1e10


class Antenna:
    """Instatiate a ground station with all its parameters
    Gain,EIRP, Usable Frequencies, Efficiencies, Dish Diameter"""

    def __init__(self,dia,EIRP,eta,f,power,noise):
        self.dia   = 70      # diameter in metres
        self.EIRP  = 1000    # effective isotropic radiated power
        self.freq  = 27*10^9 # frequency used in the radar in Hz
        self.eta   = 0.55    # overall efficiency of the radar
        self.power = 1000    # power in watts
        self.noise = 1200    # noise temperature in Deg K

    def Gain(self):
        return 10*log10(self.eta*(pi*self.dia*self.freq/c)^2)


class Celestialbody:
    def __init__(self,radius,GM,orb_radius,flatness):
        self.radius = 3678.131 # Earth Radius in km
        self.GM = 398600 # Gravitational Parameter in km^3/sec^2
        self.orb_radius = 149.598 * 1e6 # Orbital radius around a central body
        self.flatness = 0.003353 # Flattening, assumed none in version 1

class Groundstation:
    # Ground stations are defined based on three parameters latitude, longitude and height
    # Possible ideas for next versions: choose the central body
    # The default values represent the Cebreros station 
    
    def __init__(self,lat,long,height):
        self.lat    = 40.4535 # Latitude in degrees
        self.long   =-4.3683  # Longitude in degrees
        self.height = 794     # height in metres    
        self.elev   = 10      # elevation in degrees


class Signal:
    # S band :  2 -  4 GHz 
    # Ka band: 26 - 40 GHz
    # Ku band: 12 - 18 GHz

    # Modulation Schemes   =  "BPSK" or "QPSK"
    # Encryption Algorithm = "" or ""
    # Scrambling Technique =  " " or ""

    """Encryption is done to cipher the sending code. This protects the privacy of the information included in the signal. Since Alan Turing first
    used his computer to break the German Encryption codes allowing for the allies to win the war, there's a race between hackers and encryption standards. 
    In the first version, we'll start with a basic encryption algorithm and increase complexity as the time proceeds"""

    """Scrambling is done to avoid interference between signals of same frequency bands"""
    def __init__(self, freq, bandwidth, modulation, encryption, scramble):
        self.freq = ""
        self.bandwidth = ""
        self.modulation = ""
        self.encryption = ""
        self.scramble = ""
    
    def modulation(self): # if there's a name conflict change the name
        pass

    def encryption(self): # if there's a name conflict then change the name
        pass

    def scramble(self): # if there's a name conflict then change the name
        pass
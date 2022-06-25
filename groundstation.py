

class Groundstation:
    # Ground stations are defined based on three parameters latitude, longitude and height
    # Possible ideas for next versions: choose the central body
    # The default values represent the Cebreros station 
    
    def __init__(self,lat,long,height,elev):
        self.lat    = 40.4535 # Latitude in degrees
        self.long   =-4.3683  # Longitude in degrees
        self.height = 794     # height in metres    
        self.elev   = 10      # elevation in degrees

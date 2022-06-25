"""
 
Antenna Acronym    Station        (lat,  long  , height in km ,  elev)

DS54                Madrid        (355.7459032,40.4256217,0.837051,15)
DS55                Madrid        (355.7473667,40.4242959,0.819061,15)
DS61                Madrid        (355.7510720,40.4287445,0.848658,15)
DS63                Madrid        (355.7519914,40.4312097,0.864816,15)
DS65                Madrid        (355.7493011,40.4272064,0.833854,15)
DS66                Madrid        (355.7485824,40.4299749,0.849874,15)
 """



class Groundstation:
    # Antennas in a ground station are defined based on three parameters latitude, longitude and height
    # In teh ground station, different antennas will have different coordinates
    # Elevation is the minimum angular height of the satellite to be visible from the ground station. Default value: 15 deg but feel free to choose a suitable value
    # Possible ideas for next versions: choose the central body
    # The default values represent the Cebreros station 
    
    def __init__(self,lat,long,height,elev):
        self.lat    = lat       # Latitude in degrees
        self.long   = long      # Longitude in degrees
        self.height = height    # height in km    
        self.elev   = elev      # elevation in degrees

        
# Sample use case
Canberra = Groundstation(355.7485824,40.4299749,0.849874,15)
print(Canberra.lat)

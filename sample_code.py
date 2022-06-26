# Using ground station class

Canberra = Groundstation(355.7485824,40.4299749,0.849874,15) # lat,long,height,elevation
print(Canberra.lat,Canberra.long,Canberra.height,Canberra.elev)



# Using text2signal
# Run the program, it prompts for a input and generates a binary plot



# Using Antenna class
ant =  Antenna(70,1000,27*10^9,0.55) # diameter, EIRP, frequency, total antenna efficiency
print(ant.dia, ant.EIRP, ant.freq, ant.eta)



# Encrypt only text with no spaces, no symbols
encrypted_text = encryption("Thisissecret","qwdf")
print(encrypted_text)
